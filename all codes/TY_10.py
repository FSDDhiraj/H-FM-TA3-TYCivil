# Given values
basin_area_km2 = 8640 # in km^2
rainfall_cm = 10 # effective rainfall in cm
base_period_days = 20 # in days
# Convert units
basin_area_m2 = basin_area_km2 * 1e6 # km^2 to m^2
rainfall_m = rainfall_cm / 100 # cm to m
base_period_seconds = base_period_days * 24 * 60 * 60 # days to seconds
# Compute runoff volume (Volume = Area x Rainfall depth)
runoff_volume_m3 = basin_area_m2 * rainfall_m
# Triangular hydrograph volume formula: Volume = 1/2 * Qp * base_period
# Solving for Qp (peak discharge)
Qp = (2 * runoff_volume_m3) / base_period_seconds
# Output result
print(f"Peak discharge (Qp) = {Qp:.2f} m³/s")