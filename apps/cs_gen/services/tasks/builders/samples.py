import json
import os

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


class SampleBuilder:

    def __init__(self) -> None:
        self._load_samples()

    def _load_samples(self) -> list[dict[str, str]]:
        
        with open(os.path.join(BASE_DIR,'phrases.json'), 'r') as file:
            samples = json.load(file)
        
        self._we: list[dict[str, str]] = samples['WordExclusion']
        self._sa: list[str] = samples['SymbolAmount']
        self._names: list[str] = samples['Names']

    def get_we_samples(self) -> list[dict[str, str]]:
        return self._we
    
    def get_sa_samples(self) -> list[str]:
        return self._sa
    
    def get_names(self) -> list[str]:
        return self._names


samples = SampleBuilder()