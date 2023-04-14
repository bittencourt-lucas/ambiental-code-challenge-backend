from typing import Tuple
from httpx import Response
from datetime import datetime


class FormatForecastJob:
    @staticmethod
    def execute(data: Tuple[Response, datetime]) -> dict:
        response, timestamp = data
        hourly_entries: dict = response.json()["hourly"]

        valid_entries: list
        valid_entries = process_wind_direction_entries(hourly_entries)
        valid_entries = process_wind_speed_entries(valid_entries)

        return {"ultima_consulta": timestamp, "dados": valid_entries}


def process_wind_direction_entries(entries: dict) -> list:
    processed_entries: list = []
    for index, entry in enumerate(entries["winddirection_180m"]):
        if is_wind_direction_dangerous(entry):
            processed_entries.append({
                "data": entries["time"][index],
                "vel": entries["windspeed_180m"][index],
                "dir": entries["winddirection_180m"][index],
                "alerta": False,
            })
    return processed_entries


def is_wind_direction_dangerous(direction: int) -> bool:
    return direction >= 130 and direction <= 230


def process_wind_speed_entries(entries: list) -> list:
    for index, entry in enumerate(entries):
        if not is_wind_speed_dangerous(entry["vel"]):
            entries[index] = None
        if should_emit_alert(entry["vel"]):
            entry["alerta"] = True
    processed_entries = list(filter(None, entries))
    return processed_entries


def is_wind_speed_dangerous(speed: int) -> bool:
    return speed >= 15


def should_emit_alert(speed: int) -> bool:
    return speed > 20
