import random

from .base_builder import AbstractTaskBuilder

from apps.cs_gen.services.tasks.encoding_tasks import (
    WordExclusionExercise,
    TextValueExercise,
    SymbolAmountExercise
)
from apps.cs_gen.services.tasks.builders.samples import samples
from apps.cs_gen.choices import ENCODINGS


ENCODINGS = [enc for enc in ENCODINGS.values()]


class WordExclusionExerciseBuilder(AbstractTaskBuilder):

    TEMPLATE = (
        "В одной из кодировок {encoding} "
        "каждый символ кодируется {bits} битами. "
        "{student} написал текст (в нём нет лишних пробелов): "
        "«{words} {phrase}». "
        "Ученик вычеркнул из списка одно слово. "
        "Заодно он вычеркнул ставшие лишними запятые и пробелы "
        "— два пробела не должны идти подряд."
        "При этом размер нового предложения в данной кодировке "
        "оказался на {bytes_diff} байт меньше, "
        "чем размер исходного предложения. "
        "Напишите в ответе вычеркнутое слово. "
    )
   
    def build_task(self) -> WordExclusionExercise:
        exercise = WordExclusionExercise(self.TEMPLATE)

        name = random.choice(samples.get_names())
        sample = random.choice(samples.get_we_samples())

        exercise.set_student_name(name)
        exercise.set_phrase(sample['phrase'])
        exercise.set_words(sample['words'])
        exercise.set_encoding(random.choice(ENCODINGS))
        exercise.set_answer(random.choice(sample['words']))

        return exercise


class TextValueExerciseBuilder(AbstractTaskBuilder):

    TEMPLATE = (
        "Статья, набранная на компьютере, "
        "содержит {page_amount} страниц, "
        "на каждой странице {string_amount} строки, "
        "в каждой строке {symbol_amount} символов. "
        "В одном из представлений {encoding} "
        "каждый символ кодируется {bits} битами. "
        "Определите информационный объём статьи "
        "в Кбайтах в этом варианте представления {encoding}."
        )
    
    PAGE_CHOICES = range(4, 129, 4)
    STRING_CHOICES = range(16, 129, 16)
    SYMBOL_CHOICES = range(16, 129, 16)
    
    def build_task(self) -> TextValueExercise:
        exercise = TextValueExercise(self.TEMPLATE)

        exercise.set_page_amount(random.choice(self.PAGE_CHOICES))
        exercise.set_string_amount(random.choice(self.STRING_CHOICES))
        exercise.set_symbol_amount(random.choice(self.SYMBOL_CHOICES))
        exercise.set_encoding(random.choice(ENCODINGS))

        return exercise


class SymbolAmountExerciseBuilder(AbstractTaskBuilder):

    TEMPLATE = (
        "В одной из кодировок {encoding} "
        "каждый символ кодируется {bits} битами. "
        "Определите размер в байтах следующего предложения "
        "в данной кодировке: {sentence}"
    )
    
    def build_task(self) -> SymbolAmountExercise:
        exercise = SymbolAmountExercise(self.TEMPLATE)

        exercise.set_encoding(random.choice(ENCODINGS))
        exercise.set_sentence(random.choice(samples.get_sa_samples()))

        return exercise
