base_hours = 40  # hours
peak_flow = 150  # m^3/s
catchment_area_km2 = 550  # km^2 (updated)

# Convert units
base_seconds = base_hours * 3600  # convert hours to seconds
catchment_area_m2 = catchment_area_km2 * 1e6  # convert km^2 to m^2

# Calculate volume of runoff (triangular hydrograph)
runoff_volume_m3 = 0.5 * base_seconds * peak_flow  # Volume of runoff in m³

# Calculate effective rainfall in meters
effective_rainfall_m = runoff_volume_m3 / catchment_area_m2  # Volume / area gives depth in meters

# Convert to millimeters
effective_rainfall_mm = effective_rainfall_m * 1000  # Convert to mm

# Output the result
print(f"Effective Rainfall: {effective_rainfall_mm:.2f} mm")
