import json
from typing import Any

from src.utils import load_transactions_from_json


def test_load_transactions_valid(tmp_path: Any) -> None:
    file_path = tmp_path / "test.json"
    data = [{"id": 1, "amount": 100}]
    file_path.write_text(json.dumps(data), encoding="utf-8")

    result = load_transactions_from_json(str(file_path))
    assert result == data


def test_load_transactions_not_found() -> None:
    result = load_transactions_from_json("non_existent_file.json")
    assert result == []


def test_load_transactions_invalid_json(tmp_path: Any) -> None:
    file_path = tmp_path / "invalid.json"
    file_path.write_text("not a json", encoding="utf-8")

    result = load_transactions_from_json(str(file_path))
    assert result == []


def test_load_transactions_not_a_list(tmp_path: Any) -> None:
    file_path = tmp_path / "dict.json"
    file_path.write_text('{"key": "value"}', encoding="utf-8")

    result = load_transactions_from_json(str(file_path))
    assert result == []
