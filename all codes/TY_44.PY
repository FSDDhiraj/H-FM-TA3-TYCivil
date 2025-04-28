def calculate_outlet_discharge(cca_hectares, intensity_percentage, kor_period_days, kor_depth_mm):
    area_under_cultivation_hectares = (intensity_percentage / 100) * cca_hectares
    area_under_cultivation_sqm = area_under_cultivation_hectares * 10000  # 1 hectare = 10,000 m²
    kor_depth_m = kor_depth_mm / 1000  # mm to m
    volume_of_water_cubic_meters = area_under_cultivation_sqm * kor_depth_m
    kor_period_seconds = kor_period_days * 24 * 60 * 60  # days to seconds
    outlet_discharge_cumecs = volume_of_water_cubic_meters / kor_period_seconds
    return outlet_discharge_cumecs

# Given values
cca = 20000  # hectares
intensity = 50  # %
kor_period = 30  # days
kor_depth = 120  # mm

# Calculate the outlet discharge
discharge = calculate_outlet_discharge(cca, intensity, kor_period, kor_depth)

# Print the result
print(f"The outlet discharge for the distributary should be approximately: {discharge:.2f} cubic meters per second (cumecs)")
