import pandas as pd
import glob
import os

# Step 1: Load all CSVs
def load_data():
    all_files = glob.glob("temperatures/stations_group_*.csv")
    dfs = []
    for file in all_files:
        year = int(os.path.basename(file).split("_")[-1].split(".")[0])
        df = pd.read_csv(file)
        df["Year"] = year
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)

# Step 2: Reshape wide → long
def reshape_data(df):
    month_order = [
        "January","February","March","April","May","June",
        "July","August","September","October","November","December"
    ]
    df_long = df.melt(
        id_vars=["STATION_NAME","STN_ID","LAT","LON","Year"],
        value_vars=month_order,
        var_name="Month", value_name="Temp"
    )
    return df_long

# Step 3: Seasonal averages
def seasonal_averages(df_long):
    month_to_season = {
        "December":"Summer","January":"Summer","February":"Summer",
        "March":"Autumn","April":"Autumn","May":"Autumn",
        "June":"Winter","July":"Winter","August":"Winter",
        "September":"Spring","October":"Spring","November":"Spring"
    }
    df_long["Season"] = df_long["Month"].map(month_to_season)

    seasonal_avg = df_long.groupby("Season")["Temp"].mean().round(1)

    order = ["Summer", "Autumn", "Winter", "Spring"]
    with open("average_temp.txt", "w", encoding="utf-8") as f:
        for season in order:
            if season in seasonal_avg.index:
                f.write(f"{season}: {seasonal_avg[season]}°C\n")
    print("Saved seasonal averages → average_temp.txt")

# Step 4: Temperature range
def temp_range(df_long):
    stats = df_long.groupby("STATION_NAME")["Temp"].agg(["min", "max"])
    stats["range"] = stats["max"] - stats["min"]

    max_range = stats["range"].max()
    winners = stats[stats["range"] == max_range]

    with open("largest_temp_range_station.txt", "w", encoding="utf-8") as f:
        for station, row in winners.iterrows():
            f.write(
                f"{station}: Range {row['range']:.1f}°C "
                f"(Max: {row['max']:.1f}°C, Min: {row['min']:.1f}°C)\n"
            )
    print("Saved largest range → largest_temp_range_station.txt")

# Step 5: Stability (std dev)
def stability(df_long):
    station_std = df_long.groupby("STATION_NAME")["Temp"].std()

    min_std = station_std.min()
    max_std = station_std.max()

    most_stable = station_std[station_std == min_std]
    most_variable = station_std[station_std == max_std]

    with open("temperature_stability_stations.txt", "w", encoding="utf-8") as f:
        for station, std in most_stable.items():
            f.write(f"Most Stable: {station}: StdDev {std:.1f}°C\n")
        for station, std in most_variable.items():
            f.write(f"Most Variable: {station}: StdDev {std:.1f}°C\n")
    print("Saved stability results → temperature_stability_stations.txt")

# Run all steps
if __name__ == "__main__":
    df = load_data()
    df_long = reshape_data(df)
    seasonal_averages(df_long)
    temp_range(df_long)
    stability(df_long)
