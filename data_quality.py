import numpy as np
import pandas as pd


def load_data(file_path):
    return pd.read_csv(file_path)


def clean_data(data):
    cleaned = data.copy()
    cleaned = cleaned.drop_duplicates()

    numeric_columns = [
        "engine_temp_c",
        "oil_pressure_bar",
        "battery_voltage_v",
        "brake_wear_percent",
    ]

    for column in numeric_columns:
        cleaned[column] = pd.to_numeric(cleaned[column], errors="coerce")
        cleaned[column] = cleaned[column].fillna(cleaned[column].median())

    return cleaned


def validate_measurements(data):
    checked = data.copy()

    checked["engine_temp_check"] = np.where(
        checked["engine_temp_c"] <= 110, "OK", "CHECK"
    )
    checked["oil_pressure_check"] = np.where(
        checked["oil_pressure_bar"] >= 2.5, "OK", "CHECK"
    )
    checked["battery_check"] = np.where(
        checked["battery_voltage_v"] >= 11.8, "OK", "CHECK"
    )
    checked["brake_wear_check"] = np.where(
        checked["brake_wear_percent"] <= 80, "OK", "CHECK"
    )

    check_columns = [
        "engine_temp_check",
        "oil_pressure_check",
        "battery_check",
        "brake_wear_check",
    ]

    checked["number_of_issues"] = (
        checked[check_columns] == "CHECK"
    ).sum(axis=1)

    checked["diagnostic_status"] = np.where(
        checked["number_of_issues"] == 0,
        "OK",
        "CHECK",
    )

    return checked


def create_quality_report(raw_data, checked_data):
    return pd.DataFrame(
        {
            "metric": [
                "Raw rows",
                "Clean rows",
                "Duplicate rows removed",
                "Missing values in raw data",
                "Rows with diagnostic issues",
            ],
            "value": [
                len(raw_data),
                len(checked_data),
                len(raw_data) - len(raw_data.drop_duplicates()),
                int(raw_data.isna().sum().sum()),
                int((checked_data["diagnostic_status"] == "CHECK").sum()),
            ],
        }
    )
