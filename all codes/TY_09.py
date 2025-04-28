# Input
area = float(input("Enter area in hectares: "))
depth_supplied = float(input("Enter depth of water supplied at field (in cm): "))
depth_stored = float(input("Enter depth of water stored in root zone (in cm): "))
transit_loss_percent = float(input("Enter percentage of water lost in transit: "))
actual_crop_use = float(input("Enter actual water used by crop in ha-m: "))

# Convert cm to m
depth_supplied_m = depth_supplied / 100
depth_stored_m = depth_stored / 100

# Calculate volumes
volume_supplied = area * depth_supplied_m
volume_stored = area * depth_stored_m
volume_diverted = volume_supplied / (1 - (transit_loss_percent / 100))

# Efficiencies
conveyance_eff = (volume_supplied / volume_diverted) * 100
application_eff = (volume_stored / volume_supplied) * 100
use_eff = (actual_crop_use / volume_diverted) * 100

# Outputs
print("\n--- Irrigation Efficiencies ---")
print(f"Water Conveyance Efficiency: {conveyance_eff:.2f}%")
print(f"Water Application Efficiency: {application_eff:.2f}%")
print(f"Water Use Efficiency: {use_eff:.2f}%")
