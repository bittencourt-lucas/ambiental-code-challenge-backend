import abc


class JobRunner(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def execute():
        raise NotImplementedError
