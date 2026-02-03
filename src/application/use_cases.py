from src.domain.entities import ComputeTask, CarbonFootprint
from src.application.ports import CarbonEstimatorPort

class EstimateEmissionUseCase:
    """
    Application Service/Use Case to coordinate the estimation.
    """
    
    def __init__(self, estimator: CarbonEstimatorPort):
        self._estimator = estimator
        
    def execute(self, task: ComputeTask) -> CarbonFootprint:
        # Use Case logic could go here (e.g., logging, validation, caching)
        return self._estimator.predict(task)
