from datetime import datetime, timedelta

CURRENT_TIMESTAMP = datetime.now()


data: dict = {
    "ultima_consulta": CURRENT_TIMESTAMP,
    "dados": [
        {
            "data": CURRENT_TIMESTAMP + timedelta(hours=2),
            "vel": 15,
            "dir": 130,
            "alerta": False,
        },
        {
            "data": CURRENT_TIMESTAMP + timedelta(hours=3),
            "vel": 20,
            "dir": 140,
            "alerta": True,
        },
        {
            "data": CURRENT_TIMESTAMP + timedelta(hours=3),
            "vel": 18,
            "dir": 150,
            "alerta": False,
        },
    ]
}
