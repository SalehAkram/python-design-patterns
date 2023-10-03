from abc import ABC, abstractmethod


class ISubject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class SubjectBase(ISubject):
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self.get_notification_payload())

    @abstractmethod
    def get_notification_payload(self):
        pass


class NewScientist(SubjectBase):

    def get_notification_payload(self):
        return "New issue of New Scientist magazine is available"


class WorldSoccer(SubjectBase):

    def get_notification_payload(self):
        return "New issue of World Soccer magazine is available"
