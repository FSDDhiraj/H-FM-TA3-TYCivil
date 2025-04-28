import numpy as np


def calculate_effective_rainfall(base_hours, peak_discharge_cms, catchment_area_km2): 
    base_seconds = base_hours * 3600  # Convert base duration from hours to seconds
    runoff_volume_m3 = 0.5 * base_seconds * peak_discharge_cms  # Calculate runoff volume
    catchment_area_m2 = catchment_area_km2 * (1000**2)  # Convert km² to m²
    runoff_depth_m = runoff_volume_m3 / catchment_area_m2  # Calculate runoff depth in meters
    effective_rainfall_cm = runoff_depth_m * 100  # Convert runoff depth to cm
    return effective_rainfall_cm 

# Given values
base = 60  # hours
peak_discharge = 100  # m³/s
area = 500  # km²

# Calculate effective rainfall
effective_rainfall = calculate_effective_rainfall(base, peak_discharge, area)

# Display
