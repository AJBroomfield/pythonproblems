import pytest
import fibonacci

def test_fib_zero():
    assert fibonacci.f(0) == 0
def test_fib_one():
    assert fibonacci.f(1) == 1
def test_fib_seven():
    assert fibonacci.f(7) == 13
def test_fib_float():
    assert fibonacci.f(7.3) == 'Not a valid data type'
def test_fib_negative():
    assert fibonacci.f(-5) == "Not a valid data type"
def test_fib_complex():
    assert fibonacci.f(6-2j) == "Not a valid data type"
def test_fib_negative():
    assert fibonacci.f('Sixty three') == "Not a valid data type"