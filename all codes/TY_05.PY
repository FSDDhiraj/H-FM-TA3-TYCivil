def calculate_runoff(C, I, A):
    # Convert area in hectares to square meters
    A_m2 = A * 10000
    Q = 0.278 * C * I * A_m2  # Runoff calculation in m³/s
    return Q

# Example input
C = 0.6  # Runoff coefficient
I = 50   # Rainfall intensity in mm/hr
A = 20   # Area in hectares

# Calculate runoff
Q = calculate_runoff(C, I, A)

# Print result
print(f"Peak Runoff Rate (Q) = {Q:.2f} m³/s")
