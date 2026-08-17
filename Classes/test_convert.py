from class022 import convert
import pytest

def test_conversion():
    assert convert(1) == 149597870700
    assert convert(50) == 7479893535000

def test_error():
    with pytest.raises(TypeError): # inside of this block, i wait one TypeError
        convert('1') # if I try put a str

def test_float_conversion():
    assert convert(0.001) == pytest.approx(149597870.691, abs = 0.1) # to pytest allow a little intolerance (0.1) with this value, allow an aproximate