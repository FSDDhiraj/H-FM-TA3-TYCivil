catchment_area_km2 = 300  # in km² 
rainfall_depth_cm = 50  # in cm 
runoff_volume_m3 = 3e7  # in m³ 

# Converting units 
catchment_area_m2 = catchment_area_km2 * 1e6  # km² to m² 
rainfall_depth_m = rainfall_depth_cm / 100  # cm to m 

# Calculating total rainfall volume 
total_rainfall_volume_m3 = catchment_area_m2 * rainfall_depth_m 

# Calculating percentage runoff 
percentage_runoff = (runoff_volume_m3 / total_rainfall_volume_m3) * 100

# Output 
print(f"Percentage of rainfall that became runoff: {percentage_runoff:.2f}%")
