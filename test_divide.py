import pytest
from calculator import divide

def test_divide_normal():
    assert divide(10, 2) == 5.0
    assert divide(9, 3) == 3.0

def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
