import matplotlib.pyplot as plt

# Given data
rainfall_rates = [12.5, 17.5, 22.5, 7.5]  # cm/h
phi_index = 7.5  # cm/h
interval_fraction = 0.25  # 15 minutes = 0.25 hours

# Calculate runoff for each interval
runoffs = []
for rate in rainfall_rates:
    if rate > phi_index:
        runoff = (rate - phi_index) * interval_fraction
    else:
        runoff = 0
    runoffs.append(runoff)

# Total runoff
total_runoff = sum(runoffs)
print(f"Total Runoff = {total_runoff:.2f} cm")

# Visualization
intervals = ['0-15 min', '15-30 min', '30-45 min', '45-60 min']

plt.figure(figsize=(8, 5))
plt.bar(intervals, runoffs, color='lightgreen', edgecolor='black')
plt.title('Runoff per 15-Minute Interval')
plt.xlabel('Time Interval')
plt.ylabel('Runoff (cm)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
