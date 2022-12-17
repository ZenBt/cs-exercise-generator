from django.db.models import IntegerChoices


class SupportedExerciseType(IntegerChoices):
    ENCODING_TASK = (0, "Задача на кодировку")
    PATH_TASK = (1, "Задача на построение абсолютного пути")


class SupportedEncoding(IntegerChoices):
    KOI = (0, "КОИ-8")
    UTF16 = (1, "UTF-16")
    UTF32 = (2, "UTF-32")
    UNICODE = (3, "Unicode")
    WIN1251 = (4, "Windows-1251")

ENCODINGS = {
    SupportedEncoding.KOI: {
        "name": "КОИ-8",
        "bits": 8
    },
    SupportedEncoding.UTF16: {
        "name": "UTF-16",
        "bits": 16 
    },
    SupportedEncoding.UTF32: {
        "name": "UTF-32",
        "bits": 32
    },
    SupportedEncoding.UNICODE: {
        "name": "Unicode",
        "bits": 16
    },
    SupportedEncoding.WIN1251: {
        "name": "Windows-1251",
        "bits": 8
    }
}