# Bank Widget

Проект для отображения последних успешных банковских операций клиента.

## Установка

1. Установите Poetry.
2. Клонируйте репозиторий.
3. Установите зависимости:
   ```bash
   poetry install

## Генераторы

Модуль `src.generators` содержит функции для эффективной работы с большими объемами транзакций.

### Фильтрация по валюте
```python
from src.generators import filter_by_currency

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))