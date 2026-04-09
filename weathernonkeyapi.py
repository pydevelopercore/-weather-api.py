import requests

def get_weather(city: str) -> dict:
    # Step 1: Geocode city name to lat/lon
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo_resp = requests.get(geo_url, params={"name": city, "count": 1}).json()

    if not geo_resp.get("results"):
        raise ValueError(f"City '{city}' not found.")

    result = geo_resp["results"][0]
    lat, lon = result["latitude"], result["longitude"]

    # Step 2: Fetch current weather
    weather_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": ["temperature_2m", "relative_humidity_2m", "wind_speed_10m", "weathercode"],
        "timezone": "auto",
    }
    weather = requests.get(weather_url, params=params).json()
    current = weather["current"]

    return {
        "city": result["name"],
        "country": result.get("country", ""),
        "temperature_c": current["temperature_2m"],
        "humidity_%": current["relative_humidity_2m"],
        "wind_kmh": current["wind_speed_10m"],
    }


if __name__ == "__main__":
    data = get_weather("Delhi")
    print(f"{data['city']}, {data['country']}")
    print(f"  Temperature : {data['temperature_c']}°C")
    print(f"  Humidity    : {data['humidity_%']}%")
    print(f"  Wind        : {data['wind_kmh']} km/h")
