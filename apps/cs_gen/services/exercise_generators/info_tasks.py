import random

from .base_generator import AbstractExerciseGenerator

from apps.cs_gen.services.tasks.base_task import AbstractTask
from apps.cs_gen.services.tasks.builders.base_builder import AbstractTaskBuilder
from apps.cs_gen.services.tasks.builders.info_builder import (
    FileStorageExerciseBuilder,
    FileTransferExerciseBuilder,
)


class FileStorageExerciseTaskGenerator(AbstractExerciseGenerator):
    
    SUPPORTED_SUBTYPES = [FileStorageExerciseBuilder,]
    
    def __init__(self, amount: int) -> None:
        self._amount = amount
        self._tasks = []
    
    
    def generate(self) -> list[AbstractTask]:
        for i in range(self._amount):
            builder = self._make_random_subtype_builder()
            self._tasks.append(
                builder.build_task()
            )
        
        return self._tasks
            
    def _make_random_subtype_builder(self) -> AbstractTaskBuilder:
        subtype_builder = random.choice(self.SUPPORTED_SUBTYPES)
        builder = subtype_builder()
        
        return builder


class FileTransferTaskGenerator(FileStorageExerciseTaskGenerator):
    
    SUPPORTED_SUBTYPES = [FileTransferExerciseBuilder,]