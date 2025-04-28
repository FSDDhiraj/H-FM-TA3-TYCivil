# Given
basin_area_km2 = 8640  # km²  
effective_rainfall_cm = 10  # cm  
base_period_days = 20  # days

# Conversions
base_period_hours = base_period_days * 24  # days to hours
base_period_seconds = base_period_hours * 3600  # hours to seconds

# Volume of 1 cm rainfall (in cubic meters)
volume_m3 = basin_area_km2 * 1e6 * 0.01  # area (m²) * rainfall depth (m)

# Peak discharge for 1 cm effective rainfall (in cubic meters per second)
peak_discharge_unit_m3_per_s = (2 * volume_m3) / base_period_seconds  # formula correction: base_period_seconds^3 to base_period_seconds

# Peak discharge for 10 cm effective rainfall (in cubic meters per second)
peak_discharge_DHR_m3_per_s = peak_discharge_unit_m3_per_s * effective_rainfall_cm  # scaling by 10 cm effective rainfall

# Display the result
print(f"Peak discharge of DRH = {peak_discharge_DHR_m3_per_s:.2f} m³/s")
