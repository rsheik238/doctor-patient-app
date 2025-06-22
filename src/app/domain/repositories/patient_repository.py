from abc import ABC, abstractmethod
from typing import List
from app.domain.models import Patient

class PatientRepository(ABC):
    @abstractmethod
    def add(self, name: str) -> Patient: ...
    @abstractmethod
    def get_all(self) -> List[Patient]: ...
