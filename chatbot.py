import telebot
import openai
import os

# 🔑 токен Telegram-бота
TELEGRAM_TOKEN = "8483022366:AAF9FAJLp38hrBnT78Qm5ugXhW-f8Gh5LTk"

# 🔑 токен OpenAI (с платформы platform.openai.com)
OPENAI_API_KEY = "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"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
openai.api_key = OPENAI_API_KEY

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Я бот с ChatGPT 🤖. Задай мне вопрос!")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # Отправляем запрос в OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # можно gpt-4o-mini, если доступен
            messages=[
                {"role": "system", "content": "Ты — дружелюбный помощник."},
                {"role": "user", "content": message.text}
            ]
        )
        reply = response["choices"][0]["message"]["content"]
        bot.send_message(message.chat.id, reply)
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка: {e}")

print("Бот запущен...")
bot.infinity_polling()
