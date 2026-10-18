from datetime import datetime
from typing import Any


def filter_by_state(
    data: list[dict[str, Any]], state: str = "EXECUTED"
) -> list[dict[str, Any]]:
    return [item for item in data if item.get("state") == state]


def sort_by_date(
    data: list[dict[str, Any]], reverse: bool = True
) -> list[dict[str, Any]]:
    return sorted(
        data, key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse
    )
