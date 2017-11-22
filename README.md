# Casimiro

> 'Soy Casimiro, y vengo a analizar tu comportamiento humano,
> *sondas radioactivas activadas*
> Túmbate y relájate escuchando el profundo sonido de mi voz...

## ¿Qué es Casimiro?

Casimiro es un pequeño bot para Telegram programado (si se puede llamar a esto programar) en Python gracias a la <a href="https://github.com/eternnoir/pyTelegramBotAPI">API pyTelegramBotApi</a>.

## ¿Qué necesitas?

Para empezar a utilizarlo con tu propio bot necesitas obtener un <a href="https://core.telegram.org/bots#3-how-do-i-create-a-bot">Token de Telegram</a>

A continuación debes instalar <strong>Python 3<strong> y las distintas dependencias que vamos a utilizar:

><a href="https://www.python.org/downloads/">Python</a>

``` bash
# Dependencias
$ pip install pyTelegramBotApi
$ pip install urllib3
```

## Configuración

En Casimiro.py debes añadir tu propio TOKEN generado por el <i>BotFather</i> de Telegram.
```python
import telebot

TOKEN = 'tu_token'
bot = telebot.TeleBot(TOKEN)
```

## Iniciar el bot

Una vez configurado puedes iniciar el bot desde la terminal:

``` bash
# Lanzar el bot
$ python Casimiro.py
```
