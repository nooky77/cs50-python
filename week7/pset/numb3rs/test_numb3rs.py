from numb3rs import validate

def test_nbr():
    assert validate("192.168.1.254") == True
    assert validate("1156.200.232.44") == False
    assert validate("2.1680.1.56") == False
    assert validate("100.168.1150.240") == False
    assert validate("100.168.115.2400") == False
    assert validate('127.500.420.720') == False
    assert validate("192.168.10.254.156") == False
    assert validate("192") == False
    assert validate("one.2.3.4") == False
    assert validate("cat") == False
