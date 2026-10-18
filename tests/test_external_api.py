from unittest.mock import MagicMock, patch

from src.external_api import get_transaction_amount_in_rub


def test_get_amount_rub() -> None:
    transaction = {"operationAmount": {"amount": "100.50", "currency": {"code": "RUB"}}}
    result = get_transaction_amount_in_rub(transaction)
    assert result == 100.50


@patch("src.external_api.requests.get")
def test_get_amount_usd(mock_get: MagicMock) -> None:
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"rates": {"RUB": 90.0}}
    mock_get.return_value = mock_response

    transaction = {"operationAmount": {"amount": "100.0", "currency": {"code": "USD"}}}
    result = get_transaction_amount_in_rub(transaction)

    assert result == 9000.0
    mock_get.assert_called_once()
