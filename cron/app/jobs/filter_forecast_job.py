from typing import Tuple
from httpx import Response
from datetime import datetime


class FilterForecastJob:
    @staticmethod
    def execute(data: Tuple[Response, datetime]) -> dict:
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
    return direction >= 130 and direction <= 230


def process_wind_speed_entries(entries: list) -> list:
    return [{
        "data": entry["data"],
        "vel": entry["vel"],
        "dir": entry["dir"],
        "alerta": should_emit_alert(entry["vel"]),
    } for entry in entries
        if is_wind_speed_dangerous(entry["vel"])]


def is_wind_speed_dangerous(speed: int) -> bool:
    return speed >= 15


def should_emit_alert(speed: int) -> bool:
    return speed > 20
