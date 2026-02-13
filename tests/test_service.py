from app.service import evaluate_status

def test_status_should_be_green():
    assert evaluate_status() == "green", "PYTHON_PYTEST_EXPECTED_GREEN"
