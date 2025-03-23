from main import average_temperature, is_comfortable, check_extremes

def test_average_temperature():
    temps = [20.0, 22.0, 24.0]
    result = average_temperature(temps)
    assert round(result, 2) == 22.00

def test_is_comfortable():
    temps = [19.0, 26.0, 22.5]
    result = is_comfortable(temps)
    assert result == [True, False, True]

def test_check_extremes_true():
    temps = [15.0, 22.0, 29.0]
    assert check_extremes(temps) == True

def test_check_extremes_false():
    temps = [18.0, 21.0, 24.0]
    assert check_extremes(temps) == False