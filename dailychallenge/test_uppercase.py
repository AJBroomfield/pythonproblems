import pytest
import uppercase

def test_uppercase_single():
    assert uppercase.upper_letters('Hello world!') ==[("H",0)]
    assert uppercase.upper_letters('hello World!') ==[("W",6)]
    assert uppercase.upper_letters('hello worlD!') ==[("D",10)]
def test_uppercase_doubleletter():
    assert uppercase.upper_letters('heLLo world!') ==[("L",2),("L",3)]
def test_uppercase_all():
    assert uppercase.upper_letters('HELLO WORLD!') ==[("H",0),("E",1),("L",2),("L",3),("O",4),("W",6),("O",7),("R",8),("L",9),("D",10)]
def test_uppercase_none():
    assert uppercase.upper_letters('hello world!') ==[]
def test_uppercase_numbers():
    assert uppercase.upper_letters('123456789!') == []
