import pytest
import alphasort

def test_uniquewords():
    assert alphasort.alphasort("just keep swimming") == "just keep swimming"
def test_alloneword():
    assert alphasort.alphasort("oneword oneword oneword oneword oneword oneword") == "oneword"
def test_includecomma():
    assert alphasort.alphasort("Frankly, my dear, I don't give a damn") == "a damn dear don't Frankly give I my"
def test_includenumbers():
    assert alphasort.alphasort("6 Blue Flowers 2 red thorns") == "2 6 Blue Flowers red thorns"
