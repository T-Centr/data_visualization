import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams


rcParams['figure.figsize'] = 12, 8
data = pd.read_csv(
    "https://video.ittensive.com/python-advanced/weather-moscow.txt",
    delimiter="\t", names=["Month", "Day", "Year", "F"]
)

data["Date"] = data.astype(str).Year + "-" + data.astype(str).Month + "-" + \
               data.astype(str).Day
data["C"] = (data["F"] - 32) / 1.8
data = data.set_index("Date")
data.index = pd.to_datetime(data.index)
data["C"]["2012-01":"2012-12"].plot()
plt.show()

data["2012-01"].reset_index().set_index("Day")["C"].plot(
    color="blue", label="Январь")
data["2012-07"].reset_index().set_index("Day")["C"].plot(
    color="red", label="Июль")
plt.legend()
plt.show()
