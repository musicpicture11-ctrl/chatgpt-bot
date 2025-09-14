import telebot
import openai
import os

import os
TELEGRAM_TOKEN = os.getenv("TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
openai.api_key = OPENAI_API_KEY

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Я бот с ChatGPT 🤖. Задай мне вопрос!")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        from openai import OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

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
