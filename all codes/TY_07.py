# Given for U1
peak_discharge_U1 = 60  # m³/s
catchment_area_U1 = 216  # km²

# For U2
peak_discharge_U2 = 120  # m³/s

# Volume for unit hydrograph (1 cm runoff) = (Catchment area × 10^6 m²) × 0.01 m
volume_U1 = catchment_area_U1 * 1e6 * 0.01  # in m³

# Volume of triangular hydrograph = (1/2) * base_width (seconds) * peak_discharge (m³/s)
# So base_width = (2 * volume) / peak_discharge
base_width_seconds = (2 * volume_U1) / peak_discharge_U1  # in seconds

# Convert base width to hours
base_width_hours = base_width_seconds / 3600  # convert seconds to hours

# Since both U1 and U2 have the same base width
# Calculate the new catchment area for U2
# volume = (1/2) * base_width * peak_discharge_U2
volume_U2 = 0.5 * base_width_seconds * peak_discharge_U2  # in m³

# catchment_area_U2 = volume / (0.01 m × 10^6 m²/km²)
catchment_area_U2 = volume_U2 / (1e6 * 0.01)  # in km²

# Output the results
print(f"Base width = {base_width_hours:.1f} hours")
print(f"Catchment area for U2 = {catchment_area_U2:.0f} km²")
