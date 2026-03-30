# 🌤️ Weather CLI

Консольный погодник с кэшированием. Быстрый прогноз для любого города.

## ✨ Возможности

- 🚀 Мгновенный ответ — кэш на 10 минут
- 🎨 Красивый вывод с эмодзи
- 🔄 Принудительное обновление `--force`
- 🔐 Безопасное хранение API-ключа

## 📦 Установка

```bash
git clone https://github.com/fivsky/weather-cli.git
cd weather-cli
pip install -r requirements.txt

🔑 Получение ключа
Зарегистрируйтесь на weatherapi.com

Скопируйте API-ключ

Создайте файл .env:

text
API_KEY=ваш_ключ_сюда

🛠️ Использование
bash
python weather.py Москва
python weather.py London --force

📁 Структура
text
weather-cli/
├── weather.py       # Основной код
├── cache.py         # Кэширование
├── .env             # API-ключ (не в git)
├── requirements.txt
└── README.md

📝 Лицензия
MIT
