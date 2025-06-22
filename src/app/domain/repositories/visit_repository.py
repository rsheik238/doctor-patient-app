from abc import ABC, abstractmethod
from typing import List
from app.domain.models import Visit

class VisitRepository(ABC):
    @abstractmethod
    def add(self, doctor_name: str, patient_name: str, date: str, time: str) -> Visit: ...
    @abstractmethod
    def get_all(self) -> List[Visit]: ...
