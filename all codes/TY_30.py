# Rainfall at adjacent stations
rainfall_A = 37
rainfall_B = 42
rainfall_C = 49

# Arithmetic Mean Method: average of the nearby stations
estimated_rainfall_X = (rainfall_A + rainfall_B + rainfall_C) / 3

print("Estimated rainfall at gauge X using Arithmetic Method:", 
      round(estimated_rainfall_X, 2), "mm")
