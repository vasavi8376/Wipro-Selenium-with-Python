import pytest

def div(a, b):
    return a/b

def test_div_zero():
    # Verify that a ZeroDivisionError is raised
    with pytest.raises(ZeroDivisionError) as exc_info:
        div(5, 0)
    # Optional: verify the error message
    assert str(exc_info.value) == "division by zero"