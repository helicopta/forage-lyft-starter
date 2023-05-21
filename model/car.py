from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def needs_service(self):
        pass
