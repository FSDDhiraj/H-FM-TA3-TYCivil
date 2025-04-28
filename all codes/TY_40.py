# Given values
duty = 432 # hectares/cumec
base_period = 150 # days
# Conversion factor
conversion_factor = 8.64
# Calculate delta in centimeters
delta_cm = (conversion_factor * base_period) / duty
# Convert delta to meters (optional)
delta_m = delta_cm / 100
# Output the results
print(f"Duty of the crop (D): {duty} hectares/cumec")
print(f"Base period of the crop (B): {base_period} days")
print(f"Delta of the crop (Δ): {delta_cm:.2f} cm")
print(f"Delta of the crop (Δ): {delta_m:.4f} m")