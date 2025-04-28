# Given values
A1 = 216 # km²
Qp1 = 60 # m³/s
Qp2 = 120 # m³/s
# Constants
runoff_volume_per_cm = 10000 # m³/km²
seconds_per_hour = 3600
# Calculate base width B (in hours)
B = (2 * runoff_volume_per_cm * A1) / (Qp1 * 
seconds_per_hour)
# Calculate A2 using B and Qp2
A2 = (0.5 * B * Qp2 * seconds_per_hour) / runoff_volume_per_cm
# Display results
print(f"Base width (B): {B} hours")
print(f"Catchment area for U2 (A2): {A2} km²")