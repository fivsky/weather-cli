import httpx
import typer
from .cache import Cache

app = typer.Typer()
cache = Cache(ttl=600)  # 10 минут

API_KEY = "296fe1beffd14bf8aa9164654262903"  # ваш ключ

def get_weather(city: str, force: bool = False):
    city_key = city.lower()
    
    # Проверка кэша
    if not force:
        cached = cache.get(city_key)
        if cached:
            return cached, None
    
    # Запрос к API
    url = "http://api.weatherapi.com/v1/current.json"
    params = {"key": API_KEY, "q": city, "lang": "ru"}
    
    response = httpx.get(url, params=params)
    
    if response.status_code == 400:
        return None, "Город не найден"
    
    if response.status_code != 200:
        return None, f"Ошибка API: {response.status_code}"
    
    data = response.json()
    current = data["current"]
    location = data["location"]
    
    text = (
        f"\n🌍 {location['name']}, {location['country']}\n"
        f"🌡 {current['temp_c']}°C (ощущается {current['feelslike_c']}°C)\n"
        f"💧 Влажность: {current['humidity']}%\n"
        f"🌬 Ветер: {current['wind_kph']} км/ч\n"
        f"☁️ {current['condition']['text']}\n"
    )
    
    # Сохраняем в кэш
    cache.set(city_key, text)
    return text, None

@app.command()
def weather(city: str, force: bool = typer.Option(False, "--force", "-f", help="Игнорировать кэш")):
    """Показать погоду для города"""
    result, error = get_weather(city, force)
    if error:
        print(f"❌ {error}")
    else:
        print(result)

if __name__ == "__main__":
    app()