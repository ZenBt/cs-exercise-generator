from django.db.models import IntegerChoices


class SupportedExerciseType(IntegerChoices):
    ENCODING_TASK = (0, "Задача на кодировку")
    PATH_TASK = (1, "Задача на построение абсолютного пути")