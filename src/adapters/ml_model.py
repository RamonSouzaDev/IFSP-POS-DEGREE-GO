
from src.domain.entities import ComputeTask, CarbonFootprint
from src.application.ports import CarbonEstimatorPort

class MLCarbonEstimator(CarbonEstimatorPort):
    """
    An ML-based (simulated) estimator for power consumption.
    
    Uses a simplified linear model based on research papers regarding
    CPU power draw vs Load.
    P_cpu = P_idle + (P_max - P_idle) * Load_percent
    """
    
    def __init__(self):
        # Simulated Hardware Specs (e.g., Intel Xeon server)
        self.p_idle_watts = 50.0
        self.p_max_watts = 250.0
        # Memory power factor (approx 0.375 W/GB)
        self.memory_w_per_mb = 0.000375 

    def predict(self, task: ComputeTask) -> CarbonFootprint:
        # 1. Calculate Power (Watts)
        # Linear Regression formula for CPU Power
        cpu_power = self.p_idle_watts + (self.p_max_watts - self.p_idle_watts) * (task.cpu_load_percent / 100.0)
        
        # Memory Power
        mem_power = task.memory_usage_mb * self.memory_w_per_mb
        
        total_power_watts = cpu_power + mem_power
        
        # 2. Calculate Energy (kWh)
        # Energy = Power * Time
        energy_kwh = (total_power_watts * task.execution_time_seconds) / (1000.0 * 3600.0)
        
        # 3. Calculate Carbon (gCO2)
        # Carbon = Energy * Intensity
        carbon_g = energy_kwh * task.carbon_intensity_g_per_kwh
        
        # 4. Contextualize
        description = self._generate_context(carbon_g)
        
        return CarbonFootprint(
            energy_kwh=round(energy_kwh, 6),
            carbon_g_co2=round(carbon_g, 4),
            impact_description=description
        )

    def _generate_context(self, carbon_g: float) -> str:
        # Simple heuristics for context
        if carbon_g < 0.1:
            return "Low impact. Like sending one email."
        elif carbon_g < 1.0:
            return "Moderate impact. Like charging a smartphone."
        elif carbon_g < 10.0:
            return "High impact. Like driving a car for ~100 meters."
        else:
            return "Significant impact. Consider optimizing this workload."
