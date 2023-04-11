import telegram
import telebot
import requests, uuid, json

#Telegram bot API token key given by BOT Father
with open("token_file.txt",'r') as f:
    api_key = f.readline().strip()

#Create the bot
bot = telebot.TeleBot(api_key)

#Setpup input message handler for the bot

#hello command
@bot.message_handler(commands=['hello'])
def hello(message):
    bot.send_message(message.chat.id,"Hi, I am the Translation Express Bot!\n"
                                     "How can I help you today?")
#start command
###letting know only SPANISH
#####
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"I can translate any English text to the Spanish")
####

#translation begin command
@bot.message_handler(commands=['translate'])
def translate(message):
    bot.reply_to(message,"Type in the English sentence you want to translate to Spanish")
    bot.register_next_step_handler(message, translation_process)

#translation process happening in this code block
def translation_process(message):
    if message.text == '/stop':
        bot.send_message(message.chat.id, "Okay, translation stopped!!!")
        return
    with open("mstranslatorkey.txt",'r') as file:
        mst_key = file.readline().strip()
    endpoint = "https://api.cognitive.microsofttranslator.com"
    location = "eastus"
    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': 'en',
        'to': 'es'
    }

    headers = {
        'Ocp-Apim-Subscription-Key': mst_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': message.text
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    message_text = response[0]['translations'][0]['text']

    bot.send_message(message.chat.id, message_text)
    bot.register_next_step_handler(message, translation_process)


#keep the bot running
bot.polling()