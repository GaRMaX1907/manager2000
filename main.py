import telebot 
from config import token
from logic import

bot = telebot.TeleBot(token)

@bot.message_handler(command = ['/start'])
def start(message):
    bot.send_message(message.chat.id, '''Вас приветствует
                    бот-менеджер интернет магазина. 
                    Для того, чтобы разобраться с тем,
                    что я умею - наберите /help''')

@bot.message_handler(command = ['/help'])
def help(message):
    bot.send_message('''Доступные команды:
                    
                    
                    ''')


bot.polling()