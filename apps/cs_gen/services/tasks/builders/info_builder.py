import random

from .base_builder import AbstractTaskBuilder
from apps.cs_gen.services.tasks.info_tasks import (
    FileStorageExercise,
    FileTransferExercise,

)


class FileStorageExerciseBuilder(AbstractTaskBuilder):
    
    TEMPLATE = (
        "Какой минимальный объём памяти (в Кбайт) "
        "нужно зарезервировать, чтобы можно было сохранить "
        "любое растровое изображение размером {width}x{height} пикселей "
        "при условии, что в изображении могут использоваться "
        "{colors} различных цветов? В ответе запишите только "
        "целое число, единицу измерения писать не нужно."
    )

    def build_task(self) -> FileStorageExercise:
        exercise = FileStorageExercise(self.TEMPLATE)

        exercise.set_width(random.choice(range(128, 2049, 128)))
        exercise.set_height(random.choice(range(128, 2049, 128)))
        exercise.set_colors(random.choice(list(map(lambda x: 2**x, range(1, 9)))))
        
        return exercise

class FileTransferExerciseBuilder(AbstractTaskBuilder):
    
    TEMPLATE = (
        "Файл размером {val} Кбайт передаётся через некоторое "
        "соединение со скоростью {sp_1} бит в секунду. "
        "Определите размер файла (в Кбайт), который можно "
        "передать за то же время через другое соединение "
        "со скоростью {sp_2} бит в секунду. В ответе "
        "укажите одно число — размер файла в Кбайт. "
        "Единицы измерения писать не нужно."
    )

    def build_task(self) -> FileTransferExercise:
        exercise = FileTransferExercise(self.TEMPLATE)

        exercise.set_val(random.choice(range(1, 1025)))
        exercise.set_sp_1(random.choice(list(map(lambda x: 2**x, range(5, 10)))))
        exercise.set_sp_2(random.choice(list(map(lambda x: 2**x, range(4, 10)))))
        
        return exercise 