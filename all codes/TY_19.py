# Given values
length_km = 100  # length of the stream in kilometers
width_m = 60     # width of the stream in meters
pan_evaporation_cm = 0.50  # pan evaporation in cm/day
pan_coefficient = 0.70  # pan coefficient

# Step 1: Convert length to meters
length_m = length_km * 1000  # 1 km = 1000 m

# Step 2: Surface area of the stream (in square meters)
surface_area_m2 = length_m * width_m  # surface area in m²

# Step 3: Actual evaporation (adjusted using pan coefficient)
actual_evaporation_cm = pan_evaporation_cm * pan_coefficient

# Step 4: Convert evaporation from cm to meters
actual_evaporation_m = actual_evaporation_cm / 100  # 1 m = 100 cm

# Step 5: Calculate mean daily evaporation loss (volume in cubic meters per day)
evaporation_loss_m3_per_day = surface_area_m2 * actual_evaporation_m

# Display the result
print(f"Mean daily evaporation loss: {evaporation_loss_m3_per_day:.2f} cubic meters/day")
