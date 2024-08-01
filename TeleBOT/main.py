import telebot
import requests

bot = telebot.TeleBot(config.TOKEN)

@bot.massage_handler(commands = ["start"])
def handle_command_start(message: telebot.types.Message):


    bot.send_message(message.chat.id, help_message)
