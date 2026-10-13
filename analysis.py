import numpy as np


def create_kpis(data):
    return {
        "Number of vehicles": data["vehicle_id"].nunique(),
        "Average engine temperature": round(
            float(np.mean(data["engine_temp_c"])), 2
        ),
        "Average oil pressure": round(
            float(np.mean(data["oil_pressure_bar"])), 2
        ),
        "Average battery voltage": round(
            float(np.mean(data["battery_voltage_v"])), 2
        ),
        "Vehicles requiring a check": int(
            (data["diagnostic_status"] == "CHECK").sum()
        ),
    }


def compare_vehicles(data):
    columns = [
        "vehicle_id",
        "engine_temp_c",
        "oil_pressure_bar",
        "battery_voltage_v",
        "brake_wear_percent",
        "number_of_issues",
        "diagnostic_status",
    ]

    return data[columns].sort_values(
        "number_of_issues",
        ascending=False,
    )
