import pytest
from calculator import add, subtract

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -5) == -6

def test_add_zero():
    assert add(0, 7) == 7

def test_subtract_positive_numbers():
    assert subtract(5, 2) == 3

def test_subtract_negative_numbers():
    assert subtract(-5, -2) == -3

def test_subtract_mixed_numbers():
    assert subtract(10, -3) == 13

def test_will_fail():
    assert False
