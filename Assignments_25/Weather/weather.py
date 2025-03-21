import requests

def get_weather(city):
    api_key = "815ad95c7568b54235f1173c9257fe36"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # To get temperature in Celsius
    }
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        
        if data['cod'] != 200:
            print("❌ City not found. Please check the name.")
            return
        
        print(f"🌍 Weather in {city}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description'].title()}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    
    except Exception as e:
        print("Error occurred:", e)

city = input("Enter city name : ")
get_weather(city)
