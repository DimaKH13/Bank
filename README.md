# Bank Widget

Проект для отображения последних успешных банковских операций клиента.

## Установка

1. Установите Poetry.
2. Клонируйте репозиторий.
3. Установите зависимости:
   ```bash
   poetry install

<<<<<<< HEAD
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
=======
## Декоратор log

Модуль `src.decorators` содержит декоратор `log` для логирования вызовов функций.

### Логирование в консоль
```python
from src.decorators import log

@log()
def my_function(x, y):
    return x + y

my_function(1, 2)

### Логирование в файл
Пример использования декоратора для записи логов в файл:

@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


## Работа с JSON и API

### Чтение данных из файла
Модуль `src.utils` содержит функцию `load_transactions_from_json` для чтения списка транзакций из JSON-файла.

### Конвертация валют
Модуль `src.external_api` содержит функцию `get_transaction_amount_in_rub` для конвертации суммы транзакции в рубли. Если валюта операции USD или EUR, функция обращается к внешнему API.

**Настройка окружения:**
Для работы функции конвертации необходим API-ключ. Создайте файл `.env` в корне проекта и добавьте в него:
```text
API_KEY=ваш_ключ_от_apilayer
