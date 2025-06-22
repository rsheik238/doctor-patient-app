from abc import ABC, abstractmethod
from typing import List
from app.domain.models import Doctor

class DoctorRepository(ABC):
    @abstractmethod
    def add(self, name: str) -> Doctor: ...
    @abstractmethod
    def get_all(self) -> List[Doctor]: ...
