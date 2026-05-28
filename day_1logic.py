sensor_data=[12,54,89,34,60,22,78,45,92,11]
filtered_data=[]
for number in sensor_data:
    if number > 50 and number%2 == 0:
        filtered_data.append(number)
if len(filtered_data) > 0:
    print(f"Successfully filtered data: {filtered_data}")
else:
    print("Error: No data found that meets the criteria.")