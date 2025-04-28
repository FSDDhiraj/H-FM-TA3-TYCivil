# Given values
base_time_hours = 60     # base of triangular hydrograph in hours
peak_flow_cms = 100      # peak discharge in cubic meters per second
catchment_area_km2 = 500 # catchment area in square kilometers

# Step 1: Convert base time to seconds
base_time_seconds = base_time_hours * 3600  # 1 hour = 3600 seconds

# Step 2: Calculate total runoff volume using triangular hydrograph formula
# Volume = (1/2) * base_time * peak_flow
runoff_volume_m3 = 0.5 * base_time_seconds * peak_flow_cms  # in cubic meters

# Step 3: Convert area to square meters (1 km² = 1,000,000 m²)
catchment_area_m2 = catchment_area_km2 * 1_000_000

# Step 4: Effective rainfall in meters
effective_rainfall_m = runoff_volume_m3 / catchment_area_m2

# Step 5: Convert to centimeters
effective_rainfall_cm = effective_rainfall_m * 100

# Final Output
print(f"Effective Rainfall = {effective_rainfall_cm:.2f} cm")
