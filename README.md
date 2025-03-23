# OpenSource-Lecture
## Indoor Temperature Analysis Utility

This small standalone Python project simulates indoor temperature readings and performs basic analysis to evaluate comfort and detect extreme values.

### 💡 Project Scope

This tool is designed to:
- Simulate indoor temperature readings (no real sensor needed)
- Calculate the average temperature from a set of readings
- Identify which readings are within a "comfortable" range (default: 18–25°C)
- Detect if any readings are extremely low or high (<16°C or >28°C)

The project is self-contained and uses no external data sources or hardware.

### 🧩 Functions Overview

#### `read_temperatures()`
Simulates and returns a list of indoor temperature readings (in Celsius).

#### `average_temperature(temps)`
Calculates and returns the average temperature from a list of values.

#### `is_comfortable(temps, min_temp=18, max_temp=25)`
Returns a list of booleans indicating whether each temperature is within the comfortable range.

#### `check_extremes(temps)`
Returns `True` if any temperature reading is considered extreme (below 16°C or above 28°C).

### 🧪 Tests

All functions have corresponding unit tests written using `pytest`, and they are automatically executed via GitHub Actions on every push or pull request.

### ✅ Requirements

- Python 3.7+
- `pytest` (for testing)

Install dependencies:

```bash
pip install -r requirements.txt
