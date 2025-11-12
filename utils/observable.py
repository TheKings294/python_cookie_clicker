from abc import ABC, abstractmethod

class Observable(ABC):
    @abstractmethod
    def subscribe(self, event_type, listener):
        pass
    @abstractmethod
    def unsubscribe(self, event_type, listener):
        pass
    @abstractmethod
    def notify(self, event_type, listener):
        pass