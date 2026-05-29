import numpy as np
print("---Array Processing---")
raw_speeds=[15.5,22.1,8.4,19.2,31.0,12.8]
speed_array=np.array(raw_speeds)
print(f"1. Packed Numpy Array: {speed_array}")
kmh_array=speed_array * 3.6
print(f"2. Vectorized Array: {kmh_array}")
high_speed_flags= kmh_array > 60.0
print(f"3. What a Mask Looks Like: {high_speed_flags}")
extreme_speed= kmh_array[high_speed_flags]
print(f"4. Filtered Results using the Mask: {extreme_speed}")
