from abc import ABC, abstractmethod

class BaseCommand(ABC):
    @abstractmethod
    def execute(self, args):
        pass
    @abstractmethod
    def help(self,args):
        pass