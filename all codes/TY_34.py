# Given values
base_time_hr = 60  # in hours
peak_flow = 150  # in m³/s
catchment_area_km2 = 425  # in km²

# Convert units
base_time_sec = base_time_hr * 3600  # convert hours to seconds
catchment_area_m2 = catchment_area_km2 * 1e6  # convert km² to m²

# Calculate volume of runoff (area under the triangular hydrograph)
volume_runoff_m3 = 0.5 * base_time_sec * peak_flow

# Calculate effective rainfall in meters
effective_rainfall_m = volume_runoff_m3 / catchment_area_m2

# Convert to cm
effective_rainfall_cm = effective_rainfall_m * 100

# Output the result
print(f"Effective rainfall of the storm is = {effective_rainfall_cm:.2f} cm")
