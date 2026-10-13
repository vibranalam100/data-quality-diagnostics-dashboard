from pathlib import Path

from analysis import create_kpis, compare_vehicles
from charts import create_diagnostic_chart
from data_quality import (
    clean_data,
    create_quality_report,
    load_data,
    validate_measurements,
)


DATA_FILE = Path("data/vehicle_measurements.csv")
OUTPUT_DIR = Path("outputs")


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    raw_data = load_data(DATA_FILE)
    clean = clean_data(raw_data)
    checked = validate_measurements(clean)

    quality_report = create_quality_report(raw_data, checked)
    kpis = create_kpis(checked)
    comparison = compare_vehicles(checked)

    checked.to_csv(
        OUTPUT_DIR / "checked_vehicle_data.csv",
        index=False,
    )

    quality_report.to_csv(
        OUTPUT_DIR / "data_quality_report.csv",
        index=False,
    )

    comparison.to_csv(
        OUTPUT_DIR / "vehicle_comparison.csv",
        index=False,
    )

    checked.to_json(
        OUTPUT_DIR / "checked_vehicle_data.json",
        orient="records",
        indent=4,
    )

    create_diagnostic_chart(
        checked,
        OUTPUT_DIR / "diagnostic_dashboard.html",
    )

    print("\nDATA QUALITY & DIAGNOSTICS DASHBOARD")
    print("------------------------------------")

    for name, value in kpis.items():
        print(f"{name}: {value}")

    print("\nFinished. Check the outputs folder.")


if __name__ == "__main__":
    main()
