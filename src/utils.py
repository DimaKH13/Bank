import json
import logging
import os
from typing import Any

os.makedirs("logs", exist_ok=True)

utils_logger = logging.getLogger("utils")
utils_logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

if not utils_logger.handlers:
    utils_logger.addHandler(file_handler)


def load_transactions_from_json(file_path: str) -> list[dict[str, Any]]:
    """Читает JSON-файл с транзакциями и возвращает список словарей."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                utils_logger.info(f"Успешно прочитан файл: {file_path}")
                return data
            utils_logger.error(f"Данные в файле {file_path} не являются списком")
            return []
    except FileNotFoundError:
        utils_logger.error(f"Файл не найден: {file_path}")
        return []
    except json.JSONDecodeError:
        utils_logger.error(f"Ошибка декодирования JSON в файле: {file_path}")
        return []