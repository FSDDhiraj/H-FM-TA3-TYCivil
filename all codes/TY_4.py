# This Python code calculates the catchment area (C.A.) in km^2
# based on the provided information about a triangular unit hydrograph.

# Given parameters:
base_time_hours = 75  # hours
peak_discharge_mps = 12  # m^3/s
unit_runoff_cm = 1  # cm

# Convert unit runoff to meters
unit_runoff_meters = unit_runoff_cm / 100

# Calculate the volume of runoff under the unit hydrograph
# The area under the triangular hydrograph represents the volume of runoff
# per unit area of the catchment.

# Area of triangle = 0.5 * base * height
# Here, base is in hours, height is in m^3/s, so the area will have units of m^3-hr/s.
# To get volume in m^3, we need to convert hours to seconds.
base_time_seconds = base_time_hours * 60 * 60

volume_runoff_m3 = 0.5 * base_time_seconds * peak_discharge_mps

# The volume of runoff is also equal to the depth of runoff over the catchment area.
# Volume = Depth * Area
# Here, Depth is the unit runoff (1 cm or 0.01 m), and Area is the catchment area (A) in m^2.

# Rearranging the formula to solve for the catchment area:
catchment_area_m2 = volume_runoff_m3 / unit_runoff_meters

# Convert the catchment area from m^2 to km^2
catchment_area_km2 = catchment_area_m2 / (1000 * 1000)

# Print the result
print(f"The catchment area (C.A.) is: {catchment_area_km2:.2f} km²")
