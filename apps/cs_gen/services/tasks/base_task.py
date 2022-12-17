from abc import ABC, abstractmethod


class AbstractTask(ABC):

    @abstractmethod
    def __init__(self, pattern: str):
        pass
    
    @abstractmethod
    def get_description(self) -> str:
        pass
    
    @abstractmethod
    def get_answer(self) -> str:
        pass