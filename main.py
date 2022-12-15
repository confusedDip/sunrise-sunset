"""Program to Check Sunrise, Sunset times using API"""
import requests
import datetime

# Define your current location
params = {
    "lat": 45.53790744833541,
    "lng": -122.90789975659347,
    "formatted": 0
}

# Make the API GET call
response = requests.get("https://api.sunrise-sunset.org/json", params=params)
response.raise_for_status()

data = response.json()

# Get the required fields
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

# Get the times
sunrise_time = sunrise.split('T')[1]
sunset_time = sunset.split('T')[1]

print(f"Sunrise at: {sunrise_time}")
print(f"Sunset at: {sunset_time}")

# Get the current time
current_datetime = datetime.datetime.utcnow()
current_time = current_datetime.time()
print(f"Current Time: {current_time}")

# Check for Sunrise and Sunset
if int(sunrise_time[:2]) <= current_time.hour <= int(sunset_time[:2]):
    print("It's Daytime!")
else:
    print("It's Night now!")
