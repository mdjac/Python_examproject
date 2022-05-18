import pytest
from Modules import textProcessingUtility as tpu

def test_hasNumbers_true():
    input = "This is a string with a number 5"
    result = tpu.has_numbers(input)
    assert result == True

def test_hasNumbers_false():
    input = "This is a string without a number"
    result = tpu.has_numbers(input)
    assert result == False

def test_any_curr_false():
    input = "This is a string without a currency"
    result = tpu.any_curr(input)
    assert result == False

def test_any_curr_true():
    input = "This is a $tring with a currency"
    result = tpu.any_curr(input)
    assert result == True

def test_translateText():
    input = [["Dette skal oversættes"]]
    result = tpu.translateText(input, srcLanguage="da",destLanguage='en')
    assert result[0][0] == "This needs to be translated"