from abc import ABC, abstractmethod
from src.domain.entities import ComputeTask, CarbonFootprint

class CarbonEstimatorPort(ABC):
    """
    Interface for the Carbon Estimation logic (Model/Adapter).
    """
    
    @abstractmethod
    def predict(self, task: ComputeTask) -> CarbonFootprint:
        """
        Predicts the carbon footprint for a given compute task.
        """
        pass
