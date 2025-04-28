def calculate_unit_hydrograph_peak(peak_flood_flow, rainfall_excess_mm, base_flow):
 """
 Calculates the peak of the unit hydrograph.
Args:
 peak_flood_flow: The peak of the flood hydrograph in m^3/sec.
 rainfall_excess_mm: The total rainfall excess in mm.
 base_flow: The constant base flow in m^3/sec.
 Returns:
 The peak of the unit hydrograph in m^3/sec/cm.
 """
 peak_direct_runoff = peak_flood_flow - base_flow
 rainfall_excess_cm = rainfall_excess_mm / 10 # Convert mm to cm
 if rainfall_excess_cm <= 0:
  return "Rainfall excess must be greater than zero."
 peak_unit_hydrograph = peak_direct_runoff / rainfall_excess_cm
 return peak_unit_hydrograph
# Given values
peak_flood = 240 # m^3/sec
rainfall = 80 # mm
base = 40 # m^3/sec
# Calculate the peak of the unit hydrograph
unit_hydrograph_peak = calculate_unit_hydrograph_peak(peak_flood, rainfall, base)
# Print the result
if isinstance(unit_hydrograph_peak, str):
 print(unit_hydrograph_peak)
else:
 print(f"The peak of the 4-hour unit hydrograph is: {unit_hydrograph_peak} m^3/sec/cm")