from dotenv import load_dotenv
from pathlib import Path
import os
import telebot

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
TOKEN = os.getenv('token')
bot = telebot.TeleBot(TOKEN)

# Respuestas automáticas


def listener(messages):
    for m in messages:
        print(m)

        if m.content_type == 'text':

            print("[" + str(m.chat.id) + " - " +
                  str(m.from_user.username) + "]: " + m.text)

            bot.send_message(m.chat.id, 'No me molestes...')


bot.set_update_listener(listener)

# Comandos


@bot.message_handler(regexp='^.*(@[cC]asimiro).*$', content_types=['text'])
def aaa(m):
    bot.reply_to(m, '¡Oye, @' + m.from_user.username + ', déjame en paz!')


@bot.message_handler(content_types=['new_chat_photo'])
def foto_nueva(m):
    print("[" + str(m.chat.id) + " - " +
          str(m.chat.title) + " - Nueva foto de perfil]: " + str(m.from_user.username) + " ha cambiado la foto")
    bot.reply_to(m, '¡Oye, @' + m.from_user.username + ', deja mi foto!')


@bot.edited_message_handler(content_types=['text'])
def mensaje_editado(m):
    print("[" + str(m.chat.id) + " - " +
          str(m.from_user.username) + " - Editado]: " + m.text + ")")
    # "(Mensaje original: " + str(m) + ")")
    bot.reply_to(m, 'Te he visto, @' + m.from_user.username)


@bot.message_handler(content_types=['location'])
def location(m):
    print("[" + str(m.chat.id) + " - " + str(m.from_user.username) + " - Ubicacion]: " + "Latitud: " +
          str(m.location.latitude) + " - Longitud: " + str(m.location.longitude))
    bot.reply_to(m, 'Ahora sé dónde estás :)')

    # Abajo esta la consola. Pulsas Control+C para parar lo que hay ahora, y cuando se pare le das a flecha arriba y a enter
    # Cada vez que hagas cambios, guardas, lo paras y lanzas de nuevo


@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, 'Soy Casimiro, y vengo a analizar tu comportamiento, humano.'
                     + ' \n*sondas radioactivas activadas*'
                     + ' \nTúmbate y relájate escuchando el profundo sonido de mi voz...')

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
