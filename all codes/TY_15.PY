# Given data
Rn = 300 # Net radiation in W/m²
T = 30 # Air temperature in °C
rho = 1000 # Density of water in kg/m³
# Compute latent heat of vaporization (kJ/kg)
L = 2501 - (2.37 * T) # kJ/kg
# Convert L from kJ/kg to J/kg (1 kJ = 1000 J)
L = L * 1000 # J/kg
# Compute evaporation rate in m/s
E_m_s = Rn / (L * rho)
# Convert evaporation rate from m/s to mm/day
E_mm_day = E_m_s * 86400000 # (1 m = 1000 mm, 1 day = 86400 s)
# Display result
print(f"Estimated evaporation rate: {E_mm_day:.2f} mm/day")