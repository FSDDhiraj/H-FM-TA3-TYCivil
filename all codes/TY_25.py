# This Python code calculates the catchment area (C.A.) in km²
# based on the provided information about a triangular unit hydrograph.

# Given parameters:
base_time_hours = 75  # hours
peak_discharge_mps = 12  # m³/s
unit_runoff_cm = 1  # cm

# Convert unit runoff to meters
unit_runoff_meters = unit_runoff_cm / 100

# Calculate the volume of runoff under the unit hydrograph
# Area of triangle = 0.5 * base * height
# Base is in hours, height is in m³/s, so need to convert base to seconds
base_time_seconds = base_time_hours * 60 * 60

# Volume in m³
volume_runoff_m3 = 0.5 * base_time_seconds * peak_discharge_mps

# Volume = Depth * Area
# Rearranging: Area = Volume / Depth
catchment_area_m2 = volume_runoff_m3 / unit_runoff_meters

# Convert the catchment area from m² to km²
catchment_area_km2 = catchment_area_m2 / (1000 * 1000)

# Print the result
print(f"The catchment area (C.A.) is: {catchment_area_km2:.2f} km²")
