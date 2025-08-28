import numpy as np

arr = np.array([1.2, 2.5, 3.8, 4.1, 5.9])
print(f"Original array: {arr}\n")

scaler_value01 = 5
addition = np.add(arr, scaler_value01)
print(f"Addition with 5: {addition}\n")

scaler_value02 = 2
multiplication = np.multiply(arr, scaler_value02)
print(f"Multiplication by 2: {multiplication}\n")

round_values = np.around(arr)
print(f"Rounded values: {round_values}\n")

floor_values = np.floor(arr)
print(f"Floor: {floor_values}\n")

ceil_values = np.ceil(arr)
print(f"Ceil: {ceil_values}\n")

natural_log = np.log(arr)
print(f"Natural log: {natural_log}\n")

log_10 = np.log10(arr)
print(f"Log10: {log_10}\n")

summition = np.sum(arr)
print(f"Sum: {summition}\n")

product = np.prod(arr)
print(f"Product: {product}\n")


def mysquare(x, y):
    return x * y


mysquare = np.frompyfunc(mysquare, 2, 1)
print(f"Custom ufunc (square): {mysquare(arr, arr)}")
