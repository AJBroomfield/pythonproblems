import pytest
import evendigits

def test_shortseqence():
    assert evendigits.even_digits(1,2)=='2'
def test_longersequence():
    assert evendigits.even_digits(10,30)== "20, 22, 24, 26, 28"
