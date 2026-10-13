# Data Quality & Diagnostics Dashboard

Beginner-level automotive Python project.

## What it does

- Reads vehicle measurement data from CSV
- Removes duplicates
- Replaces missing numeric values with the median
- Checks simple diagnostic limits
- Calculates a few KPIs
- Compares vehicles
- Exports CSV and JSON
- Creates one interactive Plotly chart
- Uses two very small pytest tests

## Run

```bash
pip install -r requirements.txt
python main.py
```

## Run tests

```bash
pytest -v
```

## Output files

- checked_vehicle_data.csv
- checked_vehicle_data.json
- data_quality_report.csv
- vehicle_comparison.csv
- diagnostic_dashboard.html

The diagnostic thresholds are only simple educational example values.
