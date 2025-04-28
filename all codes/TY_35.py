import math


def manning_streamflow(n, a, r, s):
 """
 Calculates streamflow using Manning's equation.
 Args:
 n: Manning's roughness coefficient (unitless).
 a: Cross-sectional area of flow (m^2).
 r: Hydraulic radius (m).
 s: Slope of the energy grade line or water surface (m/m).
 Returns:
 Streamflow in cubic meters per second (m^3/s).
 """
 q = (1/n) * a * (r**(2/3)) * (s**0.5)
 return q
# Example usage
n = 0.035 # Manning's roughness coefficient for a natural channel
a = 10 # Cross-sectional area of flow in m^2
r = 2 # Hydraulic radius in m
s = 0.001 # Slope of the energy grade line
q = manning_streamflow(n, a, r, s)
print(f"The streamflow is: {q} m^3/s")