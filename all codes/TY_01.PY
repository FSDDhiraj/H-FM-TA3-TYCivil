# Given data
rainfall_cm = 2.7 # in cm
loss_rate_cm_per_hr = 0.3 # in cm/hr
duration_hr = 3 # in hours
base_flow_m3_per_s = 20 # in m³/s
peak_flow_m3_per_s = 210 # in m³/s
# Step 1: Calculate effective rainfall
total_losses_cm = loss_rate_cm_per_hr * duration_hr
effective_rainfall_cm = rainfall_cm - total_losses_cm
# Step 2: Calculate direct runoff peak flow
direct_runoff_peak_m3_per_s = peak_flow_m3_per_s - base_flow_m3_per_s
# Step 3: Calculate peak of 3-hr unit hydrograph
peak_of_unit_hydrograph = direct_runoff_peak_m3_per_s / effective_rainfall_cm
# Output the result
print(f"Peak of 3-hr unit hydrograph = {peak_of_unit_hydrograph:.2f} m³/s")