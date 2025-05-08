import requests
from django.shortcuts import render

def get_weather(request):
    payl = None  # Ensure it's always defined
    error = None  # Initialize error

    if request.method == "POST":
        city = request.POST.get('city')  # ✅ Get city name
        
        if city:  # Check if input is not empty
            api_key = "94013b1bd3a38345a908dcfc6e1f84c4"
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

            response = requests.get(url)  # ✅ Fix: use requests.get()
            if response.status_code == 200:
                data = response.json()
                payl = {
                    "city": data["name"],
                    "temp": data["main"]["temp"],
                    "feels_like": data["main"]["feels_like"],  # ✅ Feels Like Temperature
                    "humidity": data["main"]["humidity"],  # ✅ Humidity
                    "wind_speed": data["wind"]["speed"],  # ✅ Wind Speed
                }
            else:
                error = "City not found"
        else:
            error = "Please enter a city name"

    context = {"pay": payl, "error": error}
    return render(request, "index.html", context)
