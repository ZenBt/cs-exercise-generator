from .base_builder import AbstractTaskBuilder

from apps.cs_gen.services.tasks.encoding_tasks import (
    WordExclusionExercise,
    TextValueExercise,
    SymbolAmountExercise
)


class WordExclusionExerciseBuilder(AbstractTaskBuilder):

    TEMPLATE = """
        В одной из кодировок <Название кодировки> 
        каждый символ кодируется <Количество бит> битами. 
        <Имя ученика> написал(а) текст (в нём нет лишних пробелов):
        «<Слово 1>, <Слово 2>, … <Слово N>, — <Фраза>».
        Ученик вычеркнул из списка одно слово. 
        Заодно он вычеркнул ставшие лишними запятые и пробелы 
        — два пробела не должны идти подряд.
        При этом размер нового предложения в данной кодировке 
        оказался на <Количество байт> байт меньше, 
        чем размер исходного предложения.
         Напишите в ответе вычеркнутое слово.
    """
# TODO: слова и фраза генерировать заранее
# TODO: случайно выбрать слово
# TODO: на основе слова и длины фраза вставлять объем и разницу
    def __init__(self, amount: int) -> None:
        self._amount = amount
        self._task = None
    
    def build_task(self) -> WordExclusionExercise:
        pass


class TextValueExerciseBuilder(AbstractTaskBuilder):

    TEMPLATE = """
        Статья, набранная на компьютере,
        содержит {page_amount} страниц,
        на каждой странице {string_amount} строки,
        в каждой строке {symbol_amount} символов.
        В одном из представлений {encoding}
        каждый символ кодируется {bits} битами.
        Определите информационный объём статьи
        в Кбайтах в этом варианте представления {encoding}.
        """

    def __init__(self, amount: int) -> None:
        self._amount = amount
        self._task = None
    
    def build_task(self) -> TextValueExercise:
        pass


class SymbolAmountExerciseBuilder(AbstractTaskBuilder):

    TEMPLATE = ""

    def __init__(self, amount: int) -> None:
        self._amount = amount
        self._task = None
    
    def build_task(self) -> SymbolAmountExercise:
        pass