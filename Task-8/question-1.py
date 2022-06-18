import numpy as np
arr = np.array([10,11,12,13,14])
print("Original array:")
print(arr)
l = 5
new_arr = np.zeros(len(arr) + (len(arr)-1)*(l))
new_arr[::l+1] = arr
print("\nNew array:")
print(new_arr)
