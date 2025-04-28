# Given return period and number of years
T = 100  # return period in years
n = 20   # duration in years

# Probability calculations
P = 1 / T           # probability of event occurring in a single year
P_not = 1 - P       # probability of event NOT occurring in a single year

# Probability of event NOT occurring in 'n' years
P_not_n = P_not ** n

# Probability of event occurring at least once in 'n' years
P_at_least_once = 1 - P_not_n

# Display result
print(f"Probability of rainfall ≥ 50 mm occurring at least once in {n} years: {P_at_least_once:.4f}")
