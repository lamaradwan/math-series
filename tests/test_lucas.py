from series.series import lucas
#Lucas Testcases
def test_seven_lucas():
    actual = lucas(7)
    expected = 29
    assert actual == expected

def test_zero_lucas():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_one_lucas():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_negative_lucas():
    actual = lucas(-2)
    expected = "Sorry, Only positive numbers are accepted"
    assert actual == expected