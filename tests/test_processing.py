import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_operations() -> list[dict]:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T12:00:00.000000"},
        {"id": 2, "state": "CANCELED", "date": "2023-01-02T12:00:00.000000"},
        {"id": 3, "state": "EXECUTED", "date": "2023-01-03T12:00:00.000000"},
    ]


def test_filter_by_state_default(sample_operations: list[dict]) -> None:
    result = filter_by_state(sample_operations)
    assert len(result) == 2
    assert all(item["state"] == "EXECUTED" for item in result)


@pytest.mark.parametrize(
    "state, expected_len",
    [
        ("EXECUTED", 2),
        ("CANCELED", 1),
        ("PENDING", 0),
    ],
)
def test_filter_by_state_parametrized(
    sample_operations: list[dict], state: str, expected_len: int
) -> None:
    result = filter_by_state(sample_operations, state)
    assert len(result) == expected_len


def test_filter_by_state_empty() -> None:
    assert filter_by_state([]) == []


def test_sort_by_date_desc(sample_operations: list[dict]) -> None:
    result = sort_by_date(sample_operations)
    assert result[0]["id"] == 3
    assert result[-1]["id"] == 1


def test_sort_by_date_asc(sample_operations: list[dict]) -> None:
    result = sort_by_date(sample_operations, reverse=False)
    assert result[0]["id"] == 1
    assert result[-1]["id"] == 3


def test_sort_by_date_invalid_format() -> None:
    invalid_data = [{"id": 1, "state": "EXECUTED", "date": "invalid-date"}]
    with pytest.raises(ValueError):
        sort_by_date(invalid_data)
