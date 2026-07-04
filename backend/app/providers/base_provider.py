from abc import ABC, abstractmethod

from app.models.response import AnalysisResponse


class BaseProvider(ABC):

    @abstractmethod
    def analyze(
        self,
        text: str
    ) -> AnalysisResponse:
        pass