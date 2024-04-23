from fuel import convert, gauge
import pytest

def test_str():
    with pytest.raises(ValueError):
        convert("three/two")
    with pytest.raises(ValueError):
        convert("0/four")
    with pytest.raises(ValueError):
        convert("programming")
    with pytest.raises(ValueError):
        convert("")

def test_numbers():
    assert convert("1/4") == 25
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_result():
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"