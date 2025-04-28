# Given values
base_hours = 75          # Base of the triangular hydrograph in hours
peak_discharge = 12      # Peak discharge in m^3/s

# Step 1: Find Area under hydrograph (Volume of runoff)
# Since base is in hours, convert to seconds (1 hour = 3600 seconds)
base_seconds = base_hours * 3600

# Area under triangle (volume) = (1/2) * base * height
runoff_volume_m3 = 0.5 * base_seconds * peak_discharge

# Step 2: Set up equation
# runoff_volume_m3 = catchment_area_km2 * 0.01 * 10^6
# Solve for catchment_area_km2
catchment_area_km2 = runoff_volume_m3 / (0.01 * 1e6)

# Output
print(f"Catchment area = {catchment_area_km2:.2f} km²")
