# Given data for U1
A1_km2 = 216           # catchment area in km^2
Qp1 = 60               # peak discharge for U1 in m^3/s
Qp2 = 120              # peak discharge for U2 in m^3/s
runoff_depth = 0.01    # 1 cm = 0.01 m

# Convert area to m^2
A1_m2 = A1_km2 * 1e6   # 1 km^2 = 1,000,000 m^2

# Calculate volume of runoff for U1
V1 = runoff_depth * A1_m2   # volume in m^3

# Base width using volume and Qp1
# V1 = 0.5 * Base_width * Qp1 => Base_width = (2 * V1) / Qp1
Base_width_seconds = (2 * V1) / Qp1   # in seconds

# Convert base width to hours
Base_width_hours = Base_width_seconds / 3600

# Now for U2, base width is same, calculate volume
# V2 = 0.5 * Base_width * Qp2
V2 = 0.5 * Base_width_seconds * Qp2

# Catchment area for U2
# V2 = runoff_depth * A2 => A2 = V2 / runoff_depth
A2_m2 = V2 / runoff_depth
A2_km2 = A2_m2 / 1e6   # convert to km^2

# Output
print(f"Base Width: {Base_width_hours:.2f} hours")
print(f"Catchment Area for U2: {A2_km2:.2f} km²")
