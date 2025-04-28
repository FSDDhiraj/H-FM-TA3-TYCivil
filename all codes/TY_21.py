# Given data
storm_duration = 6  # hours
rainfall_intensity = 30  # mm/h (already in mm/h)
runoff_volume = 18e6  # cubic meters (Mm3 to m3)
basin_area = 240e6  # square meters (km² to m²)

# Compute total rainfall volume
rainfall_volume = rainfall_intensity * storm_duration * basin_area / 1000  
# rainfall_intensity is in mm/h, so divide by 1000 to convert mm to meters

# Compute infiltration volume
infiltration_volume = rainfall_volume - runoff_volume

# Compute average infiltration rate (in mm/h)
infiltration_rate = (infiltration_volume / (storm_duration * basin_area)) * 1000  
# convert back to mm/h

# Display result
print(f"Average infiltration rate: {infiltration_rate:.2f} mm/h")
