# Given values
P = 16               # Total rainfall in cm
tc = 12              # Rainfall duration in hours
phi_index = 0.5      # Infiltration rate in cm/hr
base_flow = 5        # Base flow in m³/sec

# 1. Calculate effective rainfall (R)
R = P - (phi_index * tc)
print(f"Effective Rainfall (R) = {R} cm")

# 2. Unit Hydrograph Ordinates
# Time (hours) vs UHG (cumecs)
time = [0, 6, 12, 18]
UHG = [0, 30, 15, 0]

# Effective Rainfall = 10 cm (from handwritten)
# DRH ordinates = UHG ordinates * (R / 1 cm)
DRH = [q * (R / 1) for q in UHG]
print(f"DRH Ordinates (m³/sec): {DRH}")

# 3. Calculate Volume of Runoff using area under DRH curve
# Approximate area under hydrograph using Trapezoidal Rule
# For each time interval of 6 hours
volume_runoff = 0
for i in range(len(time) - 1):
    volume_runoff += 0.5 * (DRH[i] + DRH[i+1]) * (time[i+1] - time[i]) * 3600  # Convert hours to seconds

print(f"Volume of Runoff = {volume_runoff:.2f} m³")

# 4. Calculate Catchment Area
# Depth of Runoff (in meters)
depth_runoff = R / 100  # convert cm to meters
area_catchment = volume_runoff / depth_runoff  # in m²
area_catchment_km2 = area_catchment / 1e6       # convert m² to km²

print(f"Area of Catchment = {area_catchment_km2:.2f} km²")
