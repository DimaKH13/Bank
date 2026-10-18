# Bank Widget

Проект для отображения последних успешных банковских операций клиента.

## Установка

1. Установите Poetry.
2. Клонируйте репозиторий.
3. Установите зависимости:
   ```bash
   poetry install

## Чтение файлов (CSV и Excel)

Модуль `src.file_readers` позволяет читать транзакции из файлов форматов CSV и Excel с помощью библиотеки `pandas`.

### Чтение из CSV
Пример использования функции `read_transactions_csv`:

transactions = read_transactions_csv("data/transactions.csv")
print(len(transactions))

### Чтение из Excel
Пример использования функции `read_transactions_excel`:

transactions = read_transactions_excel("data/transactions_excel.xlsx")
print(len(transactions))