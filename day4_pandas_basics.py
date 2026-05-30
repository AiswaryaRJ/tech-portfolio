import pandas as pd
altitudes=[120, 150, 180, 90]
altitudes_series = pd.Series(altitudes, name="Altitude_m")
print('1. Labeled Pandas Series: ')
print(altitudes_series)
print("-"*40)
telemetry_data = {

    "Battery_Pct":[98, 85, 72, 95],

    "Velocity_kmh": [45.2, 61.8, 55.0, 32.1],

    "Status": ["Optimal", "Warning", "Optimal", "Safe"]

}

df = pd.DataFrame(telemetry_data, index=["A", "B", "C", "D"])

print("2. Formatted pandas DataFrame: ")

print(df)

print("-"*40)

print("Executing the Velocity Column (Returns a Series): ")

print(df["Velocity_kmh"])
print("-"*40)