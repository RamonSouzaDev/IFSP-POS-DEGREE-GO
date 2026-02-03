from fastapi import FastAPI
from src.domain.entities import ComputeTask, CarbonFootprint
from src.adapters.ml_model import MLCarbonEstimator
from src.application.use_cases import EstimateEmissionUseCase

app = FastAPI(
    title="EcoCompute API",
    description="Green Software Engineering API to estimate Carbon Footprint of compute tasks.",
    version="1.0.0"
)

# Dependency Injection (Manual for simplicity, could use a container)
estimator_adapter = MLCarbonEstimator()
estimate_use_case = EstimateEmissionUseCase(estimator_adapter)

@app.post("/estimate", response_model=CarbonFootprint, tags=["Green Software"])
async def estimate_carbon_footprint(task: ComputeTask):
    """
    Calculate the Carbon Footprint of a computational task.
    """
    return estimate_use_case.execute(task)

@app.get("/health", tags=["System"])
async def health_check():
    return {"status": "ok", "message": "EcoCompute is Green and Running 🌿"}
