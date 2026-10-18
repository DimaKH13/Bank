from typing import Any, cast

import pandas as pd


def read_transactions_csv(file_path: str) -> list[dict[str, Any]]:
    """Читает транзакции из CSV-файла и возвращает список словарей."""
    try:
        df = pd.read_csv(file_path, sep=";")
        return cast(list[dict[str, Any]], df.to_dict(orient="records"))
    except FileNotFoundError:
        return []
    except pd.errors.EmptyDataError:
        return []


def read_transactions_excel(file_path: str) -> list[dict[str, Any]]:
    """Читает транзакции из Excel-файла и возвращает список словарей."""
    try:
        df = pd.read_excel(file_path)
        return cast(list[dict[str, Any]], df.to_dict(orient="records"))
    except FileNotFoundError:
        return []
    except ValueError:
        return []
