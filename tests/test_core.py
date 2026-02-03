import pytest
from src.domain.entities import ComputeTask
from src.adapters.ml_model import MLCarbonEstimator
from src.application.use_cases import EstimateEmissionUseCase

def test_compute_task_validation():
    """Test that ComputeTask validates input ranges."""
    # Valid
    task = ComputeTask(cpu_load_percent=50, memory_usage_mb=1024, execution_time_seconds=60)
    assert task.cpu_load_percent == 50
    
    # Invalid CPU Load > 100
    with pytest.raises(ValueError):
        ComputeTask(cpu_load_percent=110, memory_usage_mb=100, execution_time_seconds=10)

def test_carbon_estimation_logic():
    """Test the ML Adapter logic (Simulated Regression)."""
    estimator = MLCarbonEstimator()
    
    # 1. Low Load Task
    task = ComputeTask(cpu_load_percent=10, memory_usage_mb=500, execution_time_seconds=3600)
    result = estimator.predict(task)
    
    assert result.energy_kwh > 0
    assert result.carbon_g_co2 > 0
    assert "impact" in result.impact_description

def test_use_case_execution():
    """Test the full Use Case execution."""
    estimator = MLCarbonEstimator()
    use_case = EstimateEmissionUseCase(estimator)
    
    task = ComputeTask(cpu_load_percent=80, memory_usage_mb=4096, execution_time_seconds=600)
    result = use_case.execute(task)
    
    # Check if calculation seems reasonable (non-zero)
    assert result.carbon_g_co2 > 0.0
