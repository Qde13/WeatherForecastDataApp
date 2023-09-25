import requests

API_KEY = "0e7fbd1304397ea8f85b5b78f44caf97"


def get_data(place, forecast_days):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place='Tokyo', forecast_days=1))
    print(get_data(place='Tokyo', forecast_days=1))
