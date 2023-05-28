import telegram
import requests
from telegram.ext import MessageHandler, Filters

bot = telegram.Bot(token='6032754908:AAEIa97Jz_VhELJaFz62fo94eYtrCHmYG-A')

def download_video(update, context):
    url = context.message.text
    payload = {'url': url}
    response = requests.post('https://api.rapidapi.com/urltoVideoAPI_beta', data=payload, headers={'X-RapidAPI-Key': '2b40ab868cmsh106795c5c86774dp1e9a30jsn5dce32cdcbdb'}).json()
    bot.send_video(chat_id=update.effective_chat.id, video=response['url'])

dispatcher = bot.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, download_video))