import sys
import os

# Добавляем родительскую папку в путь
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from weather import get_weather
from cache import Cache

def test_cache_set_get():
    cache = Cache(ttl=1)
    cache.set("test", "value")
    assert cache.get("test") == "value"

def test_cache_expires():
    import time
    cache = Cache(ttl=1)
    cache.set("test", "value")
    time.sleep(1.1)
    assert cache.get("test") is None

def test_weather_error():
    result, error = get_weather("nonexistentcity12345", force=True)
    assert error == "Город не найден"
    assert result is None