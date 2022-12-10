from abc import ABC, abstractmethod

from apps.cs_gen.services.tasks.base_task import AbstractTask


class AbstractTaskBuilder(ABC):
    
    @abstractmethod
    def build_task(self) -> AbstractTask:
        pass
