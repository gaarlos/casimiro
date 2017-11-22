import telebot

TOKEN = 'tu_token'
bot = telebot.TeleBot(TOKEN)

def listener(messages):

  for m in messages:

    if m.content_type == 'text':
      
      bot.send_message(m.chat_id, 'No me molestes...')

@bot.message_handler(commands=['start'])

def start(m):
  bot.send_message(m.chat.id, 'Soy Casimiro, y vengo a analizar tu comportamiento, humano.' 
  +' \n*sondas radioactivas activadas*'
  +' \nTúmbate y relájate escuchando el profundo sonido de mi voz...')

bot.polling()
