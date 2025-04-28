def calculate_runoff(cn, rainfall_mm):
    """
    Calculates runoff using the SCS-CN method.
    Args: 
    cn: Curve number.
    rainfall_mm: Rainfall in millimeters.
    Returns: 
    Runoff in millimeters.
    """
    s = (25400 / cn) - 254  # Calculate the potential retention based on the curve number.
    if rainfall_mm > 0.2 * s:
        runoff_mm = ((rainfall_mm - 0.2 * s) ** 2) / (rainfall_mm + 0.8 * s)  # Calculate runoff for rainfall above 0.2S.
    else:
        runoff_mm = 0  # If the rainfall is less than 0.2S, no runoff occurs.
    return runoff_mm

def main():
    watershed_area_ha = 190  # watershed area in hectares
    cn_iii = 78  # Curve number for type III soil
    rainfall_day1_mm = 80  # Rainfall on Day 1 in mm
    rainfall_day2_mm = 58  # Rainfall on Day 2 in mm
    
    # Calculate runoff for each day
    runoff_day1_mm = calculate_runoff(cn_iii, rainfall_day1_mm)
    runoff_day2_mm = calculate_runoff(cn_iii, rainfall_day2_mm)
    
    # Convert the watershed area to square meters (1 hectare = 10,000 m²)
    watershed_area_m2 = watershed_area_ha * 1e4
    
    # Calculate total runoff volume (convert runoff from mm to meters and area from ha to m²)
    total_runoff_m3 = ((runoff_day1_mm + runoff_day2_mm) / 1000) * watershed_area_m2  # Convert mm to m
    
    # Output the results
    print(f"Runoff for Day 1: {runoff_day1_mm:.2f} mm") 
    print(f"Runoff for Day 2: {runoff_day2_mm:.2f} mm") 
    print(f"Total runoff volume: {total_runoff_m3:.2f} m³") 

# Call the main function
main()
