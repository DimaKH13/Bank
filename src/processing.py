import re
from collections import Counter
from datetime import datetime
from typing import Any


def filter_by_state(
    data: list[dict[str, Any]], state: str = "EXECUTED"
) -> list[dict[str, Any]]:
    """Фильтрует список операций по указанному статусу state."""
    return [item for item in data if item.get("state") == state]


def sort_by_date(
    data: list[dict[str, Any]], reverse: bool = True
) -> list[dict[str, Any]]:
    """Сортирует список операций по дате. По умолчанию по убыванию."""
    return sorted(
        data, key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse
    )


def process_bank_search(
    data: list[dict[str, Any]], search: str
) -> list[dict[str, Any]]:
    """Ищет транзакции по строке в описании с использованием регулярных выражений."""
    pattern = re.compile(search, re.IGNORECASE)
    return [item for item in data if pattern.search(item.get("description", ""))]


def process_bank_operations(
    data: list[dict[str, Any]], categories: list[str]
) -> dict[str, int]:
    """Считает количество операций по заданным категориям из поля description."""
    counter: Counter = Counter()
    for item in data:
        description = item.get("description", "")
        for category in categories:
            if category.lower() in description.lower():
                counter[category] += 1
    return dict(counter)
