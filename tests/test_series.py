import pytest
from series.series import fibonacci


def test_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected
