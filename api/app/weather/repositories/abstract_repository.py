import abc


class WeatherRepository(abc.ABC):
    @abc.abstractmethod
    def list_forecast(self) -> dict:
        raise NotImplementedError

    @abc.abstractmethod
    def list_alerts(self) -> dict:
        raise NotImplementedError
