from seasons import seasons
import pytest


def test_valid():
    assert (
        seasons("2022-09-30")
        == "Five hundred twenty-five thousand, six hundred minutes"
    )
    assert (
        seasons("2021-09-30") == "One million, fifty-one thousand, two hundred minutes"
    )


def test_invalid():
    with pytest.raises(SystemExit):
        seasons("test")
    with pytest.raises(SystemExit):
        seasons("01-01-2020")
    with pytest.raises(SystemExit):
        seasons("")
