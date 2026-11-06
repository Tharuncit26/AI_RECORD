# IoT Sensor Data Analysis using NumPy

import numpy as np

sensor_data = np.array([22.4, 23.8, 24.6, 26.1, 27.5,
                        28.3, 29.6, 25.9, 26.8, 30.5])

print("Sensor Data:", sensor_data)
print("Mean       :", round(np.mean(sensor_data), 2))
print("Median     :", round(np.median(sensor_data), 2))
print("Minimum    :", np.min(sensor_data))
print("Maximum    :", np.max(sensor_data))
print("Std. Dev.  :", round(np.std(sensor_data), 2))

threshold = 28.0
high_values = sensor_data[sensor_data > threshold]

print("Values above", threshold, ":", high_values)