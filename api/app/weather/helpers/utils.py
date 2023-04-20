def filter_only_alerts(current_reading: dict) -> dict:
    return {
        "ultima_consulta": current_reading["ultima_consulta"],
        "dados": [entry["data"] for entry in current_reading["dados"] if entry["alerta"] is True]
    }
