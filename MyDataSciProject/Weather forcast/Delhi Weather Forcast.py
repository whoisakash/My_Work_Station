import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

weather_data= pd.read_csv("DailyDelhiClimateTrain.csv")
print(weather_data.head())
print(weather_data.describe())
print(weather_data.info())

# figure = px.line(weather_data, x="date",
#                  y="meantemp",
#                  title="Mean Temperature in Delhi Over the Years")
# figure.show()

# figure = px.line(weather_data, x="date",
#                  y="humidity",
#                  title="Humidity in Delhi Over the Years")
# figure.show()

# figure = px.line(weather_data, x="date",
#                  y="wind_speed",
#                  title='Wind Speed in Delhi Over the Years')
# figure.show()

# figure = px.scatter(data_frame=weather_data, x="humidity",
#                     y="meantemp", size="meantemp",
#                     trendline="ols",
#                     title="Relationship Between Temperature and Humidity")
# figure.show()

weather_data["date"] = pd.to_datetime(weather_data["date"], format='%Y-%m-%d')
weather_data['year'] = weather_data['date'].dt.year
weather_data["month"] = weather_data["date"].dt.month
print(weather_data.head())

plt.style.use('fivethirtyeight')
plt.figure(figsize=(15, 10))
plt.title("Temperature Change in Delhi Over the Years")
sns.lineplot(data = weather_data, x='month', y='meantemp', hue='year')
# plt.show()

forecast_data = weather_data.rename(columns = {"date": "ds",
                                       "meantemp": "y"})
print(forecast_data)

from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
model = Prophet()
model.fit(forecast_data)
forecasts = model.make_future_dataframe(periods=365)
predictions = model.predict(forecasts)
plot_plotly(model, predictions)
