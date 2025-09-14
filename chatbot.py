import os
from openai import OpenAI
import telebot

# Загружаем токены из переменных окружения
TELEGRAM_TOKEN = os.getenv("TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Проверяем, что токены есть
if not TELEGRAM_TOKEN or not OPENAI_API_KEY:
    raise ValueError("Не найдены переменные окружения TOKEN или OPENAI_API_KEY")

# Создаем клиентов
bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = OpenAI(api_key=OPENAI_API_KEY)

# Команда /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id,
        "Привет! Я бот с ChatGPT 🤖. Я могу отвечать на твои вопросы. "
        "Просто напиши сообщение, и я постараюсь помочь!"
    )

# Обработка любых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ты — дружелюбный помощник."},
                {"role": "user", "content": message.text}
            ]
        )
        reply = response.choices[0].message.content
        bot.send_message(message.chat.id, reply)
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка: {e}")

print("Бот запущен...")
bot.infinity_polling()
