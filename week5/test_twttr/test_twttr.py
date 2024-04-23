from twttr import shorten

def test_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("facebook") == "fcbk"
    assert shorten("microsoft") == "mcrsft"

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("FACEBOOK") == "FCBK"
    assert shorten("MICROSOFT") == "MCRSFT"

def test_number():
    assert shorten("42") == "42"
    assert shorten("48152348") == "48152348"

def test_char():
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("facebook") == "fcbk"
    assert shorten("CS50") == "CS50"
    assert shorten("50") == "50"
    assert shorten("") == ""