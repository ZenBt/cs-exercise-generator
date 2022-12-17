import random

from collections import OrderedDict
from typing import Optional, Union
from .base_task import AbstractTask


class AbsolutePathExercise(AbstractTask):

    def __init__(self, pattern: str) -> None:
        self._pattern = pattern
        self._description: Optional[str] = None
        self._answer: Optional[str] = None
    
    def get_description(self) -> str:
        return self._description or self._make_description()
    
    def _make_description(self) -> str:
        self._description = self._pattern.format(
            protocol=self._protocol,
            domain_name=self._domain_name,
            domain_zone=self._domain_zone,
            filename=self._filename,
            file_extension=self._file_extension,
            variants=self._make_variants_and_answer()
        )

        return self._description
    
    def _make_variants_and_answer(self) -> str:
        
        ans = self._make_answer()

        ordered_ans = OrderedDict(sorted(ans.items(), key=lambda x: x[0]))
        
        for k, v in ordered_ans.items():
            ordered_ans[k] = f"{k}) {v}"
        
        return "\n".join(ordered_ans.values())
    
    def _make_answer(self) -> dict:
        abc = list("АБВГДЕЖ")
        ans = {}
        ans[abc.pop(random.randint(0, len(abc)-1))] = self._protocol
        ans[abc.pop(random.randint(0, len(abc)-1))] = "://"
        ans[abc.pop(random.randint(0, len(abc)-1))] = self._domain_name

        ans[abc.pop(random.randint(0, len(abc)-1))] = self._domain_zone
        ans[abc.pop(random.randint(0, len(abc)-1))] = "/"
        ans[abc.pop(random.randint(0, len(abc)-1))] = self._filename

        ans[abc.pop(random.randint(0, len(abc)-1))] = self._file_extension
        self._answer = "".join(ans.keys())
        
        return ans

    def get_answer(self) -> str:
        return self._answer

    def set_protocol(self, protocol: str) -> None:
        self._protocol = protocol
    
    def set_domain_name(self, domain_name: str) -> None:
        self._domain_name = domain_name
    
    def set_domain_zone(self, domain_zone: str) -> None:
        self._domain_zone = domain_zone
    
    def set_filename(self, filename: str) -> None:
        self._filename = filename
    
    def set_file_extension(self, file_extension: str) -> None:
        self._file_extension = file_extension
    
