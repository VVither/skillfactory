import requests
import config
import messages
from telebot import TeleBot, types

bot = TeleBot(config.TOKEN)

class ConvertionException(Exception):
    pass

class CarrencyConvertor:
    @staticmethod
    def convert(quote:str, base: str, amount :str):
    
        if quote == base:
            raise ConvertionException(f"Вы переводите одинаковые валюты!!!")
    
        try:
            quote_ticker = config.keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')
    
        try:
         base_ticker = config.keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConnectionError(f'Не удалось обработать колличество {amount}')
            
        def currency_ration():
            EXCHNGE_RATE = f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{quote_ticker}.json"
            from_currency = quote_ticker
            to_currency = base_ticker
            r = requests.get(EXCHNGE_RATE)
            if r.status_code != 200:
                return -1
            json_data = r.json()
            return json_data[from_currency][to_currency]
        ration = currency_ration() * amount
        return ration

@bot.message_handler(commands=['start', "help"])
def handle_command_start(message: types.Message):
    bot.send_message(message.chat.id, messages.start_message)

@bot.message_handler(commands=['value'])
def handle_command_value(message: types.Message):
    text = "На данный момент доступны следующие типы валют: "
    for key in config.keys.keys():
        text = "\n".join((text,key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def convert(message: types.Message):
    values = message.text.split(' ')

    if len(values) != 3:
        raise ConvertionException('Слишком много параметров,')
    
    quote, base, amount = values
    result = CarrencyConvertor.convert(quote, base, amount)
    text = f"цена {amount} {quote} в {base} = {result}"
    bot.send_message(message.chat.id, text)


bot.infinity_polling()