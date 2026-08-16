from class021 import square
import pytest

def main():
    test_negative()
    test_positive()
    test_zero()
    test_str()
    
def test_positive():
    if (square(2) != 4):
        print("2 square wasn't 4")
    if (square(3) != 9):
        print("3 square wasn't 9")

    # if I want execute 10000 tests? I use Units Tests, for example, a keyword "assert". Assert allow you to do exactly that, to assert, that something is true, not errors.
    try:
        assert square(4) == 16 # i'm affirmating, in caps lock, what 4 squared would be 16
    except AssertionError:
        print("4 square wasn't 16")

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError): # type of exception I expect in the test
        square('cat') # when typed cat, it will give TypeError

if (__name__ == '__main__'):
    main()