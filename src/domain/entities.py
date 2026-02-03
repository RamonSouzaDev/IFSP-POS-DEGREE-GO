from pydantic import BaseModel, Field

class ComputeTask(BaseModel):
    """
    Represents a computational task's resource usage.
    """
    cpu_load_percent: float = Field(..., ge=0, le=100, description="Average CPU Load (%) during execution")
    memory_usage_mb: float = Field(..., ge=0, description="Average Memory usage in Megabytes")
    execution_time_seconds: float = Field(..., ge=0, description="Duration of the task in seconds")
    carbon_intensity_g_per_kwh: float = Field(475.0, ge=0, description="Carbon intensity of the power grid (gCO2/kWh). Default is Global Avg.")

class CarbonFootprint(BaseModel):
    """
    Represents the calculated environmental impact.
    """
    energy_kwh: float = Field(..., description="Total Energy consumed in kWh")
    carbon_g_co2: float = Field(..., description="Total Carbon emissions in grams of CO2eq")
    impact_description: str = Field(..., description="Contextual description of the impact (e.g. 'Charging smartphones')")
