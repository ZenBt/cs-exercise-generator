from abc import ABC, abstractmethod

from apps.cs_gen.services.tasks.base_task import AbstractTask


class AbstractExerciseGenerator(ABC):
    
    @abstractmethod
    def __init__(self, amount: int) -> None:
        super().__init__()
    
    
    @abstractmethod
    def generate(self) -> list[AbstractTask]:
        pass
