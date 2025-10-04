import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)


url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 35.7,       # تهران
    "longitude": 51.4,      # تهران
    "hourly": "temperature_2m,relative_humidity_2m,precipitation"
}
responses = openmeteo.weather_api(url, params=params)

# Process first location
response = responses[0]
print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation: {response.Elevation()} m asl")
print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")

# Process hourly data
hourly = response.Hourly()
hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
hourly_humidity = hourly.Variables(1).ValuesAsNumpy()
hourly_precipitation = hourly.Variables(2).ValuesAsNumpy()

hourly_data = {
    "date": pd.date_range(
        start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
        end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
        freq=pd.Timedelta(seconds=hourly.Interval()),
        inclusive="left"
    ),
    "temperature_2m": hourly_temperature_2m,
    "humidity": hourly_humidity,
    "precipitation": hourly_precipitation
}



# make it a dataframe
hourly_dataframe = pd.DataFrame(data=hourly_data)
print("\nHourly data\n", hourly_dataframe.head())

# delete time zone
hourly_dataframe["date"] = hourly_dataframe["date"].dt.tz_convert(None)

# save to excel
hourly_dataframe.to_excel("tehran_weather.xlsx", index=False)
print("✅ Tehran weather saved to tehran_weather.xlsx")


hourly_dataframe.to_excel("tehran_weather.xlsx", index=False)
print("✅ Tehran weather saved to tehran_weather.xlsx")
