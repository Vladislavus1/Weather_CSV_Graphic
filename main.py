import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# reading data from csv file:
weather_data = pd.read_csv("weather_data.csv").values

# plot 1(temperature):
dates = pd.to_datetime(weather_data[:, 0])
temperatures = weather_data[:, 1].astype(int)

plt.subplot(2, 1, 1)
plt.plot(dates, temperatures)
plt.xticks(rotation=30)
plt.xlabel("Date")
plt.ylabel("Temperature (Celsius)")
plt.title("Weather Temperature")

plt.yticks(np.arange(int(max(temperatures))+1))
plt.tight_layout()

# plot 2(precipitation):
dates = pd.to_datetime(weather_data[:, 0])
precipitation = weather_data[:, 2].astype(int)

plt.subplot(2, 1, 2)
plt.plot(dates, precipitation)
plt.xticks(rotation=30)
plt.xlabel("Date")
plt.ylabel("Precipitation(mm)")
plt.title("Weather Precipitation")

plt.yticks(np.arange(int(max(precipitation))+1))
plt.tight_layout()

# displaying:
plt.show()