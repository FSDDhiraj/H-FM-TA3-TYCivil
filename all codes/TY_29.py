# Given data
time = [0, 6, 12, 18, 24, 30, 36]  # in hours
Q = [6, 18, 30, 24, 12, 8, 6]  # in m³/s
base_flow = 6  # in m³/s
catchment_area_km2 = 50  # in km²

# Step 1: Calculate DRH (Direct Runoff Hydrograph)
DRH = [q - base_flow for q in Q]

# Step 2: Time interval (delta t) in seconds
delta_t = 6 * 60 * 60  # 6 hours converted to seconds

# Step 3: Volume of Runoff using trapezoidal rule
volume_of_runoff = delta_t * ((DRH[0] + DRH[-1]) / 2 + sum(DRH[1:-1]))

# Step 4: Area of catchment in m²
catchment_area_m2 = catchment_area_km2 * 1_000_000

# Step 5: Depth of Runoff (in meters)
depth_of_runoff_m = volume_of_runoff / catchment_area_m2

# Step 6: Convert depth into centimeters
depth_of_runoff_cm = depth_of_runoff_m * 100

# Printing results
print("Volume of Runoff =", volume_of_runoff, "m³")
print("Depth of Runoff =", round(depth_of_runoff_cm, 2), "cm")
