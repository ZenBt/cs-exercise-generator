import random

from .base_builder import AbstractTaskBuilder

from apps.cs_gen.services.tasks.path_tasks import AbsolutePathExercise
from apps.cs_gen.services.tasks.builders.samples import samples


class AbsolutePathExerciseBuilder(AbstractTaskBuilder):

    TEMPLATE = (
        "Доступ к файлу {filename}{file_extension}, "
        "находящемуся на сервере {domain_name}{domain_zone}, "
        "осуществляется по протоколу {protocol}. "
        "Фрагменты адреса файла закодированы буквами от А до Ж. "
        "Запишите последовательность этих букв, "
        "кодирующую адрес указанного файла в сети Интернет. "
        "{variants}"
    )

    def build_task(self) -> AbsolutePathExercise:
        exercise = AbsolutePathExercise(self.TEMPLATE)

        exercise.set_protocol(random.choice(samples.get_protocols()))
        exercise.set_domain_name(random.choice(samples.get_domain_names()))
        exercise.set_domain_zone(random.choice(samples.get_domain_zones()))
        exercise.set_filename(random.choice(samples.get_filenames()))
        exercise.set_file_extension(random.choice(samples.get_file_extensions()))

        return exercise