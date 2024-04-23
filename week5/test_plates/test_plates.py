from plates import is_valid

def test_length():
    assert is_valid("") == False
    assert is_valid("C") == False
    assert is_valid("CS") == True
    assert is_valid("CSSA50") == True

def test_start_with_two_letters():
    assert is_valid("C") == False
    assert is_valid("2") == False
    assert is_valid("CS") == True
    assert is_valid("00") == False
    assert is_valid("C5") == False

def test_no_ponctuation():
    assert is_valid("$!#$") == False
    assert is_valid("#SAD!S") == False

def test_middle_number():
    assert is_valid("CS001") == False
    assert is_valid("CS101") == True

def test_ending_number():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False

def test_alpha():
    assert is_valid("aaa123") == True
    assert is_valid("Ab55") == True
    assert is_valid("CS50") == True
    assert is_valid("PI3.14") == False
    assert is_valid("programming") == False
    assert is_valid("AAA22A") == False
    assert is_valid("CS05") == False
    assert is_valid("57AED") == False
