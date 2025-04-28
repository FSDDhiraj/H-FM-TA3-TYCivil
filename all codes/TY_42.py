base_period_rice = 150 # in days
delta_rice = 1.3 # in meters
area_rice = 2500 # in hectares
base_period_wheat = 120 # in days
delta_wheat = 0.5 # in meters
# Step 1: Calculate Duty for Rice
duty_rice = (8.64 * base_period_rice) / delta_rice
print(f"Duty for Rice = {duty_rice:.2f} hectares/cumec")
# Step 2: Calculate Discharge (Q)
Q = area_rice / duty_rice
print(f"Discharge (Q) = {Q:.4f} cumec")
# Step 3: Calculate Duty for Wheat
duty_wheat = (8.64 * base_period_wheat) / delta_wheat
print(f"Duty for Wheat = {duty_wheat:.2f} hectares/cumec")
# Step 4: Calculate maximum permissible irrigated area for Wheat
area_wheat = Q * duty_wheat
print(f"Maximum permissible irrigated area for Wheat = {area_wheat:.1f} hectares")