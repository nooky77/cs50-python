from um import count

def test_valid():
    assert count("um") == 1
    assert count("um?") == 1

def test_valid_upper():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2

def test_invalid():
    assert count("yummy") == 0
