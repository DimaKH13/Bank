import json
from typing import Any


def load_transactions_from_json(file_path: str) -> list[dict[str, Any]]:
    """Читает JSON-файл с транзакциями и возвращает список словарей."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
