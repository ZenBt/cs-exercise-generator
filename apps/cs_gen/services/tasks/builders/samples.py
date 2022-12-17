import json
import os

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


class SampleBuilder:

    def __init__(self) -> None:
        self._load_samples()

    def _load_samples(self) -> list[dict[str, str]]:
        
        with open(os.path.join(BASE_DIR, 'samples.json'), 'r') as file:
            samples = json.load(file)
        
        self._we: list[dict[str, str]] = samples['WordExclusion']
        self._sa: list[str] = samples['SymbolAmount']
        self._names: list[str] = samples['Names']

        self._protocols: list[str] = samples['Protocol']
        self._domain_names: list[str] = samples['DomainName']
        self._domain_zones: list[str] = samples['DomainZone']
        self._filenames: list[str] = samples['FileName']
        self._file_extensions: list[str] = samples['FileExtension']

    def get_we_samples(self) -> list[dict[str, str]]:
        return self._we
    
    def get_sa_samples(self) -> list[str]:
        return self._sa
    
    def get_names(self) -> list[str]:
        return self._names
    
    def get_protocols(self) -> list[str]:
        return self._protocols
    
    def get_domain_names(self) -> list[str]:
        return self._domain_names
    
    def get_domain_zones(self) -> list[str]:
        return self._domain_zones
    
    def get_filenames(self) -> list[str]:
        return self._filenames
    
    def get_file_extensions(self) -> list[str]:
        return self._file_extensions


samples = SampleBuilder()