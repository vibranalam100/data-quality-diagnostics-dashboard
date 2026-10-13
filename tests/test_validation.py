import pandas as pd

from data_quality import validate_measurements


def test_healthy_measurement_is_ok():
    data = pd.DataFrame(
        {
            "vehicle_id": ["TEST-001"],
            "engine_temp_c": [95],
            "oil_pressure_bar": [4.0],
            "battery_voltage_v": [12.5],
            "brake_wear_percent": [40],
        }
    )

    result = validate_measurements(data)

    assert result.loc[0, "diagnostic_status"] == "OK"


def test_high_temperature_requires_check():
    data = pd.DataFrame(
        {
            "vehicle_id": ["TEST-002"],
            "engine_temp_c": [120],
            "oil_pressure_bar": [4.0],
            "battery_voltage_v": [12.5],
            "brake_wear_percent": [40],
        }
    )

    result = validate_measurements(data)

    assert result.loc[0, "engine_temp_check"] == "CHECK"
