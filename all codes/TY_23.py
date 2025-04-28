def calculate_effective_rainfall(peak_discharge, base_width_hours, catchment_area_km2):
    """
    Calculates the effective rainfall of a storm given the direct runoff hydrograph
    and catchment area.
    
    Args:
    peak_discharge: The peak discharge of the direct runoff hydrograph in m³/s.
    base_width_hours: The base width of the triangular direct runoff hydrograph in hours.
    catchment_area_km2: The catchment area in square kilometers.
    
    Returns:
    The effective rainfall of the storm in centimeters.
    """
    # Convert base width from hours to seconds
    base_width_seconds = base_width_hours * 60 * 60
    
    # Calculate the volume of runoff (area under the triangular hydrograph) in m³
    volume_of_runoff_m3 = 0.5 * base_width_seconds * peak_discharge
    
    # Convert catchment area from km² to m²
    catchment_area_m2 = catchment_area_km2 * (1000 ** 2)
    
    # Calculate the depth of runoff in meters
    depth_of_runoff_m = volume_of_runoff_m3 / catchment_area_m2
    
    # Convert the depth of runoff from meters to centimeters
    effective_rainfall_cm = depth_of_runoff_m * 100
    
    return effective_rainfall_cm

# Example Given values:
peak_discharge = 12  # m³/s
base_width_hours = 75  # hours
catchment_area_km2 = 5  # km² (example value)

# Calculate the effective rainfall
effective_rainfall = calculate_effective_rainfall(peak_discharge, base_width_hours, catchment_area_km2)

# Print the result
print(f"The effective rainfall of the storm is: {effective_rainfall:.2f} cm")
