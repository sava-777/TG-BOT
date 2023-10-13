import telebot

from config import TOKEN, TEXTS, CURRENCIES
from extensions import CurrencyConverter, APIException

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, TEXTS["welcome"])


@bot.message_handler(commands=['values'])
def send_values(message):
    values_list = [f"{k} - {v}" for k, v in CURRENCIES.items()]
    bot.send_message(message.chat.id, TEXTS["available_currencies"].format("\n".join(values_list)))


@bot.message_handler(content_types=['text'])
def convert(message):
    try:
        base, quote, amount = message.text.split()
        amount = float(amount)
        price = CurrencyConverter.get_price(base.upper(), quote.upper(), amount)
        price = round(price, 3)
        bot.reply_to(message, f"{price} {quote}")
    except APIException as e:
        bot.reply_to(message, f"Ошибка: {e}")
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {type(e).__name__} - {e}")


if __name__ == '__main__':
    print("Бот запущен")
    bot.polling()
