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
                                     "How can I help you today?\n"
                                     "Select '/start' to know more about me")
#start command

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"I can translate any English text to any of the languages that I know!\n"
                                     "Click on '/select_language' to proceed with the language selection")
####
#selecting language
@bot.message_handler(commands=['select_language'])
def select_language(message):
    bot.send_message(message.chat.id, "Enter the language code from the below list\n"
                                      "Spanish = es\n"
                                      "French = fr\n"
                                      "Hindi = hi\n"
                                      "Arabic = ar\n"
                                      "Korean = ko")
    bot.register_next_step_handler(message, language)

lang_code = ''

def language(message):
    global lang_code
    if message.text == 'es':
        lang_code = 'es'
        bot.send_message(message.chat.id, "Type in the English sentence you want to translate to Spanish")
        bot.register_next_step_handler(message, translation_process)
    elif message.text == 'fr':
        lang_code = 'fr'
        bot.send_message(message.chat.id, "Type in the English sentence you want to translate to French")
        bot.register_next_step_handler(message, translation_process)
    elif message.text == 'hi':
        lang_code = 'hi'
        bot.send_message(message.chat.id, "Type in the English sentence you want to translate to Hindi")
        bot.register_next_step_handler(message, translation_process)
    elif message.text == 'ar':
        lang_code = 'ar'
        bot.send_message(message.chat.id, "Type in the English sentence you want to translate to Arabic")
        bot.register_next_step_handler(message, translation_process)
    elif message.text == 'ko':
        lang_code = 'ko'
        bot.send_message(message.chat.id, "Type in the English sentence you want to translate to Korean")
        bot.register_next_step_handler(message, translation_process)
    else:
        bot.reply_to(message, "Entered wrong language code")
    return lang_code



#translation begin command
#@bot.message_handler(commands=['translate'])
#def translate(message):
#    bot.reply_to(message,"Type in the English sentence you want to translate to Spanish")
#    bot.register_next_step_handler(message, translation_process)

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
        'to': lang_code
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