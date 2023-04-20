import abc


class WeatherRepository(abc.ABC):
    def __init__(self, client) -> None:
        self.client = client

    @abc.abstractmethod
    def list_forecast(self) -> dict:
        raise NotImplementedError

    @abc.abstractmethod
    def list_alerts(self) -> dict:
        raise NotImplementedError
