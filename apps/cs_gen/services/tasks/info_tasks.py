import math
from typing import Optional, Union

from .base_task import AbstractTask


class FileStorageExercise(AbstractTask):
    
    def __init__(self, pattern: str) -> None:
        self._pattern = pattern
        self._description: Optional[str] = None
        self._answer: Optional[str] = None
    
    def get_description(self) -> str:
        return self._description or self._make_description()
    
    def _make_description(self) -> str:
        self._description = self._pattern.format(
            width=self._width,
            height=self._height,
            colors=self._colors
        )
        return self._description
    
    def get_answer(self) -> str:
        return self._answer or self._make_answer()

    def _make_answer(self) -> str:
        i = int(math.log2(self._colors))
        val = self._width * self._height * i
        return self._to_kb(val)

    def _to_kb(self, val: int) -> str:
        return val // 8 // 1024

    def set_width(self, width: int) -> None:
        self._width = width
    
    def set_height(self, height: int) -> None:
        self._height = height
    
    def set_colors(self, colors: int) -> None:
        self._colors = colors
        

class FileTransferExercise(AbstractTask):
    
    def __init__(self, pattern: str) -> None:
        self._pattern = pattern
        self._description: Optional[str] = None
        self._answer: Optional[str] = None
    
    def get_description(self) -> str:
        return self._description or self._make_description()
    
    def _make_description(self) -> str:
        self._description = self._pattern.format(
            val=self._val,
            sp_1=self._sp_1,
            sp_2=self._sp_2
        )
        return self._description
    
    def get_answer(self) -> str:
        return self._answer or self._make_answer()

    def _make_answer(self) -> str:
        val_1 = self._val * 8 * 1024
        t_1 = val_1 // self._sp_1
        val_2 = self._sp_2 * t_1
        return self._to_kb(val_2)
    
    def _to_kb(self, val: int) -> str:
        return val // 8 // 1024

    def set_val(self, val: int) -> None:
        self._val = val
    
    def set_sp_1(self, sp_1: int) -> None:
        self._sp_1 = sp_1
    
    def set_sp_2(self, sp_2: int) -> None:
        self._sp_2 = sp_2