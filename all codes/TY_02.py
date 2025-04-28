# Given
area_km2 = 8640 # km²
rainfall_cm = 10 # cm
base_period_days = 20 # days
base_hours = base_period_days * 24
# convert to hours
# Convert values
area_m2 = area_km2 * 1e6
rainfall_m = rainfall_cm / 100
base_seconds = base_hours * 3600
# Total runoff volume (in m³)
runoff_volume_m3 = area_m2 * rainfall_m
# Triangular hydrograph:
Volume = 0.5 * base * Qp
# Solve for Qp (peak discharge)
peak_flow = (2 * runoff_volume_m3) / base_seconds
print(f"Peak of DRH = {peak_flow:.2f} m³/s")