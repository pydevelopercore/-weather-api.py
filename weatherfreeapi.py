import requests

API_KEY = "your_api_key_here"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city: str) -> dict:
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",   # use "imperial" for °F
    }
    resp = requests.get(BASE_URL, params=params)
    resp.raise_for_status()
    data = resp.json()

    return {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temperature_c": data["main"]["temp"],
        "feels_like_c": data["main"]["feels_like"],
        "humidity_%": data["main"]["humidity"],
        "description": data["weather"][0]["description"],
        "wind_mps": data["wind"]["speed"],
    }


if __name__ == "__main__":
    data = get_weather("London")
    print(f"{data['city']}, {data['country']}")
    print(f"  {data['description'].capitalize()}")
    print(f"  Temperature : {data['temperature_c']}°C (feels like {data['feels_like_c']}°C)")
    print(f"  Humidity    : {data['humidity_%']}%")
    print(f"  Wind        : {data['wind_mps']} m/s")
