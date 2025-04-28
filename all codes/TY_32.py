# Given isohyet data: (Area in hectares, Estimated mean precipitation in inches)
isohyet_data = [
 (40, 6.2), (110, 5.5), (236, 4.5), (430, 3.5), (772, 2.5), (990, 1.5), (1010, 0.9)
]
# Calculate total weighted precipitation and total area
total_precip = 0
total_area = 0
for area, precip in isohyet_data:
 total_precip += area * precip
 total_area += area
# Mean basin precipitation
mean_precip = total_precip / total_area
# Output the result
print(f"Total Area of Basin: {total_area} ha")
print(f"Mean Basin Precipitation: {round(mean_precip, 2)} inches")