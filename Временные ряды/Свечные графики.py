import plotly.graph_objects as go
import pandas as pd
from datetime import datetime


open_data = [33.0, 33.3, 33.5]
high_data = [33.1, 33.3, 33.6]
low_data = [32.7, 32.7, 32.8]
close_data = [33.0, 32.9, 33.3]
dates = [
    datetime(year=2018, month=10, day=10),
    datetime(year=2018, month=11, day=10),
    datetime(year=2018, month=12, day=10)
]

fig = go.Figure(
    data=[go.Candlestick(x=dates, open=open_data, high=high_data, low=low_data,
                         close=close_data)]
)
fig.show()

data = pd.read_csv(
    "https://video.ittensive.com/python-advanced/finance-charts-apple.csv"
)

fig = go.Figure(
    data=[go.Candlestick(x=data['Date'], open=data['AAPL.Open'],
                         high=data['AAPL.High'], low=data['AAPL.Low'],
                         close=data['AAPL.Close'])]
)
fig.show()
