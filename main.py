import telebot

token = "854361990:AAH80QtBkwKDFljKZ-u1CIcbhU_LL0ZVXRk"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def answer_start(message):
  bot.send_message(message.chat.id, "Привет! С помощью этого бота ты можешь создать записку, который сможет прочитать лишь один человек.\nКоманды:\n/makenote - создать записку.\n/opennote - прочитать записку.\n/help - остальная полезная информация и контакты для обратной связи.")

@bot.message_handler(commands=['makenote'])
def answer_makenote(message):
  bot.send_message(message.chat.id, "Пришли мне записку и я выдам тебе ключ.")

@bot.message_handler(commands=['opennote'])
def answer_opennote(message):
  bot.send_message(message.chat.id, "Пришли мне ключ и я выдам тебе записку, только не забывай что у тебя 10 попыток.")

@bot.message_handler(commands=['help'])
def answer_help(message):
  bot.send_message(message.chat.id, "Обратная связь: t.me/mansurovv\nИнформация как пользоваться - /start")
  
bot.polling()