# tests/test_main.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Temperature import average_temperature, is_comfortable, check_extremes

def test_average_temperature():
    temps = [20.0, 22.0, 24.0]
    result = average_temperature(temps)
    assert round(result, 2) == 22.00

def test_is_comfortable():
    temps = [17.5, 22.0, 26.0]
    result = is_comfortable(temps)
    assert result == [False, True, False]

def test_check_extremes_true():
    temps = [15.0, 29.0]
    assert check_extremes(temps) is True

def test_check_extremes_false():
    temps = [18.5, 20.0, 24.0]
    assert check_extremes(temps) is False