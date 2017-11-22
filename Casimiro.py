import telebot

TOKEN = 'tu_token'
bot = telebot.TeleBot(TOKEN)

# Respuestas automáticas

def listener(messages):

  for m in messages:

    if m.content_type == 'text':

      print("[" + str(m.chat.id) + "]: " + m.text)

      bot.send_message(m.chat.id, 'No me molestes...')

bot.set_update_listener(listener)

# Comandos

@bot.message_handler(commands=['start'])

def start(m):
  bot.send_message(m.chat.id, 'Soy Casimiro, y vengo a analizar tu comportamiento, humano.' 
  +' \n*sondas radioactivas activadas*'
  +' \nTúmbate y relájate escuchando el profundo sonido de mi voz...')

# Para grupos...

@bot.message_handler(content_types=['new_chat_members'])

def new_user(m):
  nombre = m.new_chat_member.first_name
  bot.send_message(m.chat.id, 'Bienvenido al grupo, '+nombre)

@bot.message_handler(content_types=['left_chat_member'])

def left_user(m):
  nombre = m.left_chat_member.first_name
  bot.send_message(m.chat.id, 'Adiós, vaquero...')

bot.polling()
