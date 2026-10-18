import pytest

from src.decorators import log


def test_log_console_success(capsys: pytest.CaptureFixture) -> None:
    @log()
    def add(a: int, b: int) -> int:
        return a + b

    assert add(1, 2) == 3
    captured = capsys.readouterr()
    assert "add ok" in captured.out


def test_log_console_error(capsys: pytest.CaptureFixture) -> None:
    @log()
    def divide(a: int, b: int) -> float:
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError. Inputs: (1, 0), {}" in captured.out


def test_log_file_success(tmp_path: pytest.TempPathFactory) -> None:
    filepath = tmp_path / "test_log.txt"
    
    @log(filename=str(filepath))
    def add(a: int, b: int) -> int:
        return a + b

    assert add(1, 2) == 3
    assert filepath.read_text(encoding="utf-8").strip() == "add ok"


def test_log_file_error(tmp_path: pytest.TempPathFactory) -> None:
    filepath = tmp_path / "test_log_err.txt"
    
    @log(filename=str(filepath))
    def divide(a: int, b: int) -> float:
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
    assert "divide error: ZeroDivisionError. Inputs: (1, 0), {}" in filepath.read_text(encoding="utf-8")