# Given data
length_km = 80  # km
width_m = 20  # meters
evap_rate_cm_per_day = 1.5  # cm/day
pan_coefficient = 0.80
days = 30  # June has 30 days

# Convert length to meters and evaporation rate to mm/day
length_m = length_km * 1000  # km to meters
evap_rate_mm_per_day = evap_rate_cm_per_day * 10  # cm to mm

# Compute surface area
surface_area_m2 = length_m * width_m  # in square meters

# Compute total evaporation volume in cubic meters
evaporated_volume_m3 = (evap_rate_mm_per_day / 1000) * surface_area_m2 * pan_coefficient * days

# Display result
print(f"Total water evaporated from the canal in June: {evaporated_volume_m3:.2f} cubic meters")
