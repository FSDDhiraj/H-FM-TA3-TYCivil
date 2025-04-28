# Given data
Q_peak = 100
base_duration_hours = 75
catchment_area_km2 = 450
base_duration_seconds = base_duration_hours * 3600
catchment_area_m2 = catchment_area_km2 * 1e6
runoff_volume_m3 = 0.5 * Q_peak * base_duration_seconds
effective_rainfall_m = runoff_volume_m3 / catchment_area_m2
effective_rainfall_mm = effective_rainfall_m * 1000
print(f"Effective Rainfall: {effective_rainfall_mm:.2f} mm")