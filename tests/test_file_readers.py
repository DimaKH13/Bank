from typing import Any
from unittest.mock import patch

import pandas as pd

from src.file_readers import read_transactions_csv, read_transactions_excel


def test_read_transactions_csv_success(tmp_path: Any) -> None:
    file_path = tmp_path / "test.csv"
    file_path.write_text(
        "id;state;date;amount\n1;EXECUTED;2023-01-01;100\n2;PENDING;2023-01-02;200",
        encoding="utf-8",
    )
    result = read_transactions_csv(str(file_path))
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["state"] == "PENDING"


def test_read_transactions_csv_not_found() -> None:
    assert read_transactions_csv("non_existent_file.csv") == []


def test_read_transactions_excel_success(tmp_path: Any) -> None:
    file_path = tmp_path / "test.xlsx"
    df = pd.DataFrame(
        [
            {"id": 1, "state": "EXECUTED", "amount": 100},
            {"id": 2, "state": "CANCELED", "amount": 200},
        ]
    )
    df.to_excel(file_path, index=False)
    result = read_transactions_excel(str(file_path))
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["state"] == "CANCELED"


def test_read_transactions_excel_not_found() -> None:
    assert read_transactions_excel("non_existent_file.xlsx") == []


@patch("src.file_readers.pd.read_csv")
def test_read_transactions_csv_mock(mock_read_csv: Any) -> None:
    mock_df = pd.DataFrame([{"id": 99, "state": "MOCKED"}])
    mock_read_csv.return_value = mock_df

    result = read_transactions_csv("fake_path.csv")

    assert len(result) == 1
    assert result[0]["id"] == 99
    mock_read_csv.assert_called_once_with("fake_path.csv", sep=";")
