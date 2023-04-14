from typing import Tuple
from httpx import Response
from datetime import datetime


class FormatForecastJob:
    @staticmethod
    def execute(data: Tuple[Response, datetime]) -> dict:
        response, timestamp = data
        hourly_entries = response.json()["hourly"]
        valid_entries = []
        
        for index, entry in enumerate(hourly_entries["winddirection_180m"]):
            if entry >= 130 and entry <= 230:
                valid_entries.append({
                    "data": hourly_entries["time"][index],
                    "vel": hourly_entries["windspeed_180m"][index],
                    "dir": hourly_entries["winddirection_180m"][index],
                    "alerta": False,
                })
        
        for index, entry in enumerate(valid_entries):
            if entry["vel"] < 15:
                valid_entries.pop(index)
            if entry["vel"] > 20:
                entry["alerta"] = True
                
        return {"ultima_consulta": timestamp, "dados": valid_entries}
