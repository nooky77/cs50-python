from bank import value


def test_numbers():
    assert value("42") == 100
    assert value("4958") == 100


def test_hello():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("Hello, Newman") == 0
    assert value("hello, Jerry") == 0


def test_h():
    assert value("hey") == 20
    assert value("heyo") == 20


def test_mixed():
    assert value("42") == 100
    assert value("*/-*") == 100
    assert value("//CS50//") == 100
    assert value("") == 100
