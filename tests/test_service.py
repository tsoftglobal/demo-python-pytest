import pytest
from app.service import evaluate_status, process_data, validate_email


def test_status_should_be_green():
    assert evaluate_status() == "green", "PYTHON_PYTEST_EXPECTED_GREEN"


def test_status_should_be_red():
    # This test should fail due to the bug in the service
    assert evaluate_status() == "red"


def test_process_data():
    data = {"name": "John", "age": 30}
    result = process_data(data)
    assert result["processed"] is True
    assert result["name"] == "John"
    assert result["age"] == 30


def test_process_data_empty():
    data = {}
    result = process_data(data)
    assert result["processed"] is True
    assert len(result) == 1


def test_validate_email_valid():
    assert validate_email("test@example.com") is True
    assert validate_email("user.name+tag@example.co.uk") is True


def test_validate_email_invalid():
    assert validate_email("invalid-email") is False
    assert validate_email("@example.com") is False
    assert validate_email("test@") is False
    assert validate_email("") is False
