from typing import Optional, Union
from .base_task import AbstractTask


class WordExclusionExercise(AbstractTask):
    
    def __init__(self, pattern: str) -> None:
        self._pattern = pattern
        self._description = None
        self._answer = None
    
    def get_description(self) -> str:
        return self._description
    
    def get_answer(self) -> str:
        return self._answer


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
        # TODO: bytes to Kb
        return self._answer
    
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
        return self._description
    
    def get_answer(self) -> str:
        return self._answer