# Given Inputs
base_hours = 60  # Base of triangular hydrograph in hours
peak_flow = 100  # Peak flow in m³/s
catchment_area_km2 = 500  # Catchment area in km²

# Conversions
base_seconds = base_hours * 3600  # Convert base to seconds
catchment_area_m2 = catchment_area_km2 * 1_000_000  # Convert area to m²

# Calculations
volume_of_runoff = 0.5 * base_seconds * peak_flow  # Volume of runoff in m³
effective_rainfall_meters = volume_of_runoff / catchment_area_m2  # Effective rainfall in meters
effective_rainfall_mm = effective_rainfall_meters * 1000  # Convert meters to millimeters

# Output
print("------ Runoff Calculation ------")
print(f"Time (Base Width): {base_hours} hours")
print(f"Catchment Area: {catchment_area_km2} km²")
print(f"Peak Discharge: {peak_flow} m³/s")
print(f"Effective Rainfall: {effective_rainfall_mm:.2f} mm")
print("---------------------------------")
