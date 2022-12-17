from typing import Optional, Union
from .base_task import AbstractTask


class WordExclusionExercise(AbstractTask):
    
    def __init__(self, pattern: str) -> None:
        self._pattern = pattern
        self._description = None
        self._answer = None
    
    def get_description(self) -> str:
        return self._description or self._make_description()
    
    def _make_description(self) -> str:
        self._render_words()
        self._description = self._pattern.format(
            phrase=self._phrase,
            words=self._rendered_words,
            student=self._student,
            encoding=self._encoding['name'],
            bits=self._encoding['bits'],
            bytes_diff=self._calculate_bytes_difference()
        )
        return self._description
    
    def _render_words(self) -> None:
        self._rendered_words = ", ".join(self._words)

    def _calculate_bytes_difference(self) -> int:
        val_answer = len(self._answer) * self._encoding['bits']
        val_symbols = 2 * self._encoding['bits']
        return (val_answer + val_symbols) // 8
    
    def get_answer(self) -> str:
        return self._answer.capitalize()
    
    def set_answer(self, answer: str) -> None:
        self._answer = answer
    
    def set_words(self, words: list[str]) -> None:
        self._words = words
    
    def set_phrase(self, phrase: str) -> None:
        self._phrase = phrase
    
    def set_encoding(self, encoding: dict[str, Union[str, int]]) -> None:
        self._encoding = encoding
    
    def set_student_name(self, student: str) -> None:
        self._student = student


class TextValueExercise(AbstractTask):
    
    def __init__(self, pattern: str) -> None:
        self._pattern = pattern
        self._description: Optional[str] = None
        self._answer: Optional[int] = None
    
    def get_description(self) -> str:
        return self._description or self._make_description()

    def _make_description(self) -> str:
        self._description = self._pattern.format(
            page_amount=self._page_amount,
            string_amount=self._string_amount,
            symbol_amount=self._symbol_amount,
            encoding=self._encoding['name'],
            bits=self._encoding['bits']
        )
        return self._description
    
    def get_answer(self) -> str:
        return self._answer or self._calculate_answer()
    
    def _calculate_answer(self) -> int:
        overall_strings = self._page_amount * self._string_amount
        overall_symbols = overall_strings * self._symbol_amount
        self._answer = overall_symbols * self._encoding['bits']
        
        return self._to_kbytes(self._answer)
    
    def _to_kbytes(self, bits: int) -> int:
        return bits // 8 // 1024
    
    def set_page_amount(self, page_amount: int) -> None:
        self._page_amount = page_amount
    
    def set_string_amount(self, string_amount: int) -> None:
        self._string_amount = string_amount
    
    def set_symbol_amount(self, symbol_amount: int) -> None:
        self._symbol_amount = symbol_amount
    
    def set_encoding(self, encoding: dict[str, Union[str, int]]) -> None:
        self._encoding = encoding


class SymbolAmountExercise(AbstractTask):

    def __init__(self, pattern: str) -> None:
        self._pattern = pattern
        self._description = None
        self._answer = None
    
    def get_description(self) -> str:
        return self._description or self._make_description()

    def _make_description(self) -> str:
        self._description = self._pattern.format(
            sentence=self._sentence,
            encoding=self._encoding['name'],
            bits=self._encoding['bits']
        )
        return self._description
    
    def get_answer(self) -> str:
        return self._answer or self._calculate_answer()
    
    def _calculate_answer(self) -> int:
        overall_symbols = len(self._sentence)
        self._answer = overall_symbols * self._encoding['bits']
        
        return self._to_bytes(self._answer)
    
    def _to_bytes(self, bits: int) -> int:
        return bits // 8

    def set_encoding(self, encoding: dict[str, Union[str, int]]) -> None:
        self._encoding = encoding
    
    def set_sentence(self, sentence: str) -> None:
        self._sentence = sentence
    