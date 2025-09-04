README – Q2_Temperature.py

Program Overview:

This program analyses temperature data from multiple Australian weather stations stored 
in CSV files under the "temperatures" folder. Each file represents one year of data.

Main Analysis:
1. Seasonal Average Temperatures:
   - Calculates average temperature per Australian season (Summer, Autumn, Winter, Spring) 
     across all stations and years.
   - Output: average_temp.txt

2. Temperature Range:
   - Finds station(s) with the largest temperature difference (Max - Min).
   - Output: largest_temp_range_station.txt

3. Temperature Stability:
   - Finds stations with most stable (lowest std dev) and most variable (highest std dev) temperatures.
   - Output: temperature_stability_stations.txt

How It Works:
- Loads all CSV files matching "stations_group_*.csv".
- Reshapes data from wide (months) to long format.
- Maps months to Australian seasons.
- Ignores missing temperature values (NaN) in all calculations.
- Handles ties by listing all stations with the same max/min values.
- Saves all results in UTF-8 encoding to preserve the degree symbol (°C) in the output files.

Requirements:
- Python 3.x
- Pandas library

How to Run:
1. Place CSV files in "temperatures" folder.
2. Run the script:
       python Q2_Temperature.py
3. Check the three output text files.

Outputs:
average_temp.txt:
Summer: 32.1°C
Autumn: 27.3°C
Winter: 21.1°C
Spring: 27.4°C

largest_temp_range_station.txt:
BOURKE-AIRPORT-AWS: Range 24.4°C (Max: 43.0°C, Min: 18.5°C)

temperature_stability_stations.txt:
Most Stable: DARWIN-AIRPORT: StdDev 1.2°C
Most Variable: WAGGA-WAGGA-AMO: StdDev 6.9°C

Notes:
- UTF-8 encoding is used when writing files to ensure the degree symbol (°C) displays correctly.

Author:
Kamalpreet  S389008

Date:
4/09/2025
