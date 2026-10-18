import os
from typing import Any

from src.file_readers import read_transactions_csv, read_transactions_excel
from src.processing import (
    filter_by_state,
    process_bank_search,
    sort_by_date,
)
from src.utils import load_transactions_from_json
from src.widget import get_date, mask_account_card


def get_amount_and_currency(transaction: dict[str, Any]) -> tuple[float, str]:
    """Извлекает сумму и валюту из транзакции (поддерживает JSON и CSV/Excel)."""
    if "operationAmount" in transaction:
        amount_str = transaction["operationAmount"].get("amount", "0")
        currency = transaction["operationAmount"].get("currency", {}).get("code", "RUB")
        return float(amount_str), currency
    
    amount_str = str(transaction.get("amount", "0")).replace(",", ".")
    currency = transaction.get("currency_code", "RUB")
    return float(amount_str), currency


def format_transaction(transaction: dict[str, Any]) -> str:
    """Форматирует транзакцию для вывода в консоль."""
    date_str = get_date(transaction.get("date", ""))
    description = transaction.get("description", "")
    
    from_acc = transaction.get("from", "")
    to_acc = transaction.get("to", "")
    
    if from_acc and to_acc:
        accounts = f"{mask_account_card(from_acc)} -> {mask_account_card(to_acc)}"
    elif to_acc:
        accounts = f"{mask_account_card(to_acc)}"
    else:
        accounts = f"{mask_account_card(from_acc)}"
        
    amount, currency = get_amount_and_currency(transaction)
    currency_symbol = "руб." if currency == "RUB" else currency
    
    return f"{date_str} {description}\n{accounts}\nСумма: {amount} {currency_symbol}\n"


def main() -> None:
    """Основная логика программы."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    
    # 1. Выбор файла
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")
    
    choice = input("Пользователь: ")
    
    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        data = load_transactions_from_json("data/operations.json")
    elif choice == "2":
        print("Для обработки выбран CSV-файл.")
        data = read_transactions_csv("data/transactions.csv")
    elif choice == "3":
        print("Для обработки выбран XLSX-файл.")
        data = read_transactions_excel("data/transactions_excel.xlsx")
    else:
        print("Неверный выбор. Завершение программы.")
        return
        
    if not data:
        print("Не удалось загрузить данные или файл пуст.")
        return

    # 2. Фильтр по статусу (с защитой от неверного ввода)
    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        status_input = input("Пользователь: ").upper()
        
        if status_input in valid_statuses:
            data = filter_by_state(data, status_input)
            print(f'Операции отфильтрованы по статусу "{status_input}"')
            break
        else:
            print(f'Статус операции "{status_input}" недоступен.')

    # 3. Сортировка по дате
    sort_choice = input("Отсортировать операции по дате? Да/Нет\nПользователь: ").lower()
    if sort_choice in ["да", "yes", "y"]:
        order_choice = input("Отсортировать по возрастанию или по убыванию?\nПользователь: ").lower()
        reverse = True if "убыв" in order_choice else False
        data = sort_by_date(data, reverse=reverse)

    # 4. Только рублевые транзакции
    rub_choice = input("Выводить только рублевые транзакции? Да/Нет\nПользователь: ").lower()
    if rub_choice in ["да", "yes", "y"]:
        data = [t for t in data if get_amount_and_currency(t)[1] == "RUB"]

    # 5. Фильтр по слову в описании
    search_choice = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: ").lower()
    if search_choice in ["да", "yes", "y"]:
        search_word = input("Введите слово для поиска: ")
        data = process_bank_search(data, search_word)

    # 6. Вывод результата
    print("Распечатываю итоговый список транзакций...")
    if not data:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(data)}")
        for item in data:
            print("\n" + format_transaction(item))


if __name__ == "__main__":
    main()