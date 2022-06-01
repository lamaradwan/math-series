import pytest
from series.series import fibonacci

#Fibonacci Testcases
def test_six_fibonacci():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected

def test_zero_fibonacci():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_one_fibonacci():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_negative_fibonacci():
    actual = fibonacci(-3)
    expected = "Sorry, Only positive numbers are accepted"
    assert actual == expected

