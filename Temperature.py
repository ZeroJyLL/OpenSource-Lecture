"""
Indoor temperature analysis utility
This tool analyzes a list of indoor temperature readings and gives basic insights.
"""

from typing import List

def read_temperatures() -> List[float]:
    """Simulate reading indoor temperatures (°C)."""
    return [21.5, 22.0, 19.8, 24.3, 26.5, 18.2, 17.0, 23.4]

def average_temperature(temps: List[float]) -> float:
    """Return the average of the given temperature readings."""
    return sum(temps) / len(temps)

def is_comfortable(temps: List[float], min_temp: float = 18, max_temp: float = 25) -> List[bool]:
    """Check which readings are within the comfortable range (default 18–25°C)."""
    return [min_temp <= t <= max_temp for t in temps]

def check_extremes(temps: List[float]) -> bool:
    """Return True if any readings are too low (<16°C) or too high (>28°C)."""
    return any(t < 16 or t > 28 for t in temps)
def main():
    temps = read_temperatures()
    print("Temperature Indoor Readings：", temps)

    avg = average_temperature(temps)
    print(f"Average Temperature：{avg:.2f}°C")

    comfortable_flags = is_comfortable(temps)
    print("the comfortable range (default 18–25°C)：", comfortable_flags)

    if check_extremes(temps):
        print("Warning: extreme temperature readings（<16°C 或 >28°C）")
    else:
        print("Excellent: no extreme temperature readings.")

if __name__ == "__main__":
    main()