from abc import ABC, abstractmethod
from src.events import Events
from src.looks import Looks
from src.sensing import Sensing
from src.sound import Sound


class Scrython(ABC, Events, Looks, Sensing, Sound):
    @abstractmethod
    def sprites(self,):
        return []

    @abstractmethod
    def logic(self, engine):
        pass
