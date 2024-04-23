from jar import Jar
import pytest


def test_init():
    jar1 = Jar()
    assert jar1.capacity == 12
    jar2 = Jar(42)
    assert jar2.capacity == 42


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar1 = Jar()
    jar1.deposit(5)
    assert jar1.size == 5


def test_withdraw():
    jar1 = Jar()
    jar1.deposit(8)
    jar1.withdraw(3)
    assert jar1.size == 5
