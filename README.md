# Bank Widget

Проект для отображения последних успешных банковских операций клиента.

## Установка

1. Установите Poetry.
2. Клонируйте репозиторий.
3. Установите зависимости:
   ```bash
   poetry install

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