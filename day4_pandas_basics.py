import pandas as pd
altitudes=[120, 150, 180, 90]
altitudes_series = pd.Series(altitudes, name="Altitude_m")
print('1. Labeled Pandas Series: ')
print(altitudes_series)
print("-"*40)
