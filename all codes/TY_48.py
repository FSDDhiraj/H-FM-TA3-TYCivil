def calculate_delta(base_period_days, duty_hectares_per_cumec):
    """
    Calculates the delta of a crop.

    Args:
        base_period_days: The base period of the crop in days.
        duty_hectares_per_cumec: The duty of the crop in hectares per cumec.

    Returns:
        The delta of the crop in centimeters.
    """
    delta_meters = (8.64 * base_period_days) / duty_hectares_per_cumec
    delta_centimeters = delta_meters * 100
    return delta_centimeters

# Given values
base_period = 120
duty = 1728

# Calculate the delta
delta = calculate_delta(base_period, duty)

# Print the result
print(f"The delta for the crop is: {delta:.2f} cm")
