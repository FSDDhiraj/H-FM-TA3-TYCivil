def calculate_effective_rainfall(base_hours, peak_discharge_mps, catchment_area_km2):
 """
 Calculates the effective rainfall of a storm given a triangular direct runoff hydrograph.
 Args:
 base_hours (float): Base of the triangular hydrograph in hours.
 peak_discharge_mps (float): Peak discharge of the hydrograph in m³/s.
 catchment_area_km2 (float): Catchment area in km².
 Returns:
 float: The effective rainfall in millimeters.
 """
 # Convert base from hours to seconds
 base_seconds = base_hours * 3600
 # Calculate the total runoff volume (area of the triangle) in m³
 runoff_volume_m3 = 0.5 * base_seconds * peak_discharge_mps
 # Convert catchment area from km² to m²
 catchment_area_m2 = catchment_area_km2 * (1000 ** 2)
 # Calculate the effective rainfall in meters
 effective_rainfall_m = runoff_volume_m3 / catchment_area_m2
 # Convert effective rainfall from meters to millimeters
 effective_rainfall_mm = effective_rainfall_m * 1000
 return effective_rainfall_mm
# Given values from the problem
base = 60 # hours
peak = 100 # m³/s
area = 500 # km²
# Calculate the effective rainfall
effective_rainfall = calculate_effective_rainfall(base, peak, area)
# Print the result
print(f"The effective rainfall of the storm is: {effective_rainfall:.1f} mm")