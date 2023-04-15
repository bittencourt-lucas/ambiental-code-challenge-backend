from datetime import datetime
from httpx import Response


MIN_DIRECTION_DEGREES = 130
MAX_DIRECTION_DEGREES = 230
MID_RISK_SPEED_KMH = 15
HIGH_RISK_SPEED_KMH = 20


class FilterForecastJob:
    @staticmethod
    def execute(data: tuple[Response, datetime]) -> dict:
        response, timestamp = data
        hourly_entries = response.json()["hourly"]

        valid_entries = process_wind_speed_entries(
            process_wind_direction_entries(hourly_entries))

        return {"ultima_consulta": timestamp, "dados": valid_entries}


def process_wind_direction_entries(entries: dict) -> list:
    return [{
        "data": entries["time"][index],
        "vel": entries["windspeed_180m"][index],
        "dir": entry,
        "alerta": False,
    } for index, entry in enumerate(entries["winddirection_180m"])
        if is_wind_direction_dangerous(entry)]


def is_wind_direction_dangerous(direction: int) -> bool:
    return MIN_DIRECTION_DEGREES <= direction <= MAX_DIRECTION_DEGREES


def process_wind_speed_entries(entries: list) -> list:
    return [{
        "data": entry["data"],
        "vel": entry["vel"],
        "dir": entry["dir"],
        "alerta": should_emit_alert(entry["vel"]),
    } for entry in entries
        if is_wind_speed_dangerous(entry["vel"])]


def is_wind_speed_dangerous(speed: int) -> bool:
    return speed >= MID_RISK_SPEED_KMH


def should_emit_alert(speed: int) -> bool:
    return speed > HIGH_RISK_SPEED_KMH
