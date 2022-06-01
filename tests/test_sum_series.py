from series.series import sum_series
#sum_series Testcases
def test_three_seven_one_sum_series():
    actual = sum_series(3,7,1)
    expected = 9
    assert actual == expected

def test_zero_sum_series():
    actual = sum_series(0)
    expected = 0
    assert actual == expected

def test_sum_series():
    actual = sum_series(1)
    expected = 1
    assert actual == expected

def test_negative_sum_series():
    actual = sum_series(-8)
    expected = "Sorry, Only positive numbers are accepted"
    assert actual == expected

def test_with_no_args_sum_series():
    actual = sum_series(9)
    expected = 34
    assert actual == expected