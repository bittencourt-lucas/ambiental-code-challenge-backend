from tests.helpers.stored_data import data


def test_list_forecast_alerts_service():
    output = ListForecastAlertsService.execute()

    expected_output = {
        "ultima_consulta": data["ultima_consulta"],
        "dados": [entry for entry in data["dados"] if entry["alerta"] is True]
    }

    assert output == expected_output
