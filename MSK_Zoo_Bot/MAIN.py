import telebot
import questions
import config
import messages

Bot = telebot.TeleBot(config.BOT_TOKEN)

@Bot.message_handler(commands=['start'])
def handle_command_start(message: telebot.types.Message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton()
    btn2 = telebot.types.KeyboardButton()
    markup.add(btn1, btn2)
    Bot.send_message(
        message.chat.id,
        messages.start_message
    )

@Bot.message_handler(commands=['help'])
def handle_command_start(message: telebot.types.Message):
    
    Bot.send_message(
        message.chat.id,
        messages.help_message
    )

@Bot.message_handler(command=['Game'])
def start_game(message: telebot.types.Message):
    Bot.send_message(
        message.chat.id,
        messages.start_game_message
    )

@Bot.message_handler()
def game_quest(message: telebot.types.Message):
    Bot.send_message(message.chat.id, questions.first_quest_text)
    text = message.text # В переменную копируется сообщение
    if 'Азия' in text.lower():
        count = count + "A"
    if 'Европа' in text.lower():
        count = count + "E"
    if 'Южная Америка' in text.lower():
        count = count + "S"
    if 'Северная америка' in text.lower():
        count = count + "N"
    if 'Африка' in text.lower():
        count = count + "D"
    if 'Люблю холодок(Арктика, Антарктика)' in text.lower():
        count = count + "C"
    



Bot.infinity_polling(skip_pending=True)