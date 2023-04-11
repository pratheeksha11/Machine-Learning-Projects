import telegram
import telebot
import requests, uuid, json

# Telegram bot API token key given by BOT Father
with open("token_file.txt",'r') as f:
    api_key = f.readline().strip()

# Create the bot
bot = telebot.TeleBot(api_key)

# Setpup message handler for the bot
# Setting up commands for the bot

# hello command
@bot.message_handler(commands=['hello'])
def hello(message):
    bot.send_message(message.chat.id,"Hi, I am the Translation Express Bot!\n"
                                     "How can I help you today?\n"
                                     "Click on '/start' to know more about me")


# start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"I can translate any English text to the languages I know!\n"
                                     "Click on '/select_language' to proceed with the language selection")

# selecting language
@bot.message_handler(commands=['select_language'])
def select_language(message):
    bot.send_message(message.chat.id, "Enter the language code from the below list\n"
                                      "Spanish = es\n"
                                      "French = fr\n"
                                      "Hindi = hi\n"
                                      "Arabic = ar\n"
                                      "Korean = ko")
    bot.register_next_step_handler(message, language)

# processing the selected language code by the user
# storing the selected language code in a variable and processing further

selected_language_code = ''
# language codes stores in a json object
lang_codes = {
        'es': 'Spanish',
        'fr': 'French',
        'hi': 'Hindi',
        'ar': 'Arabic',
        'ko': 'Korean'
    }

# language function to let the user know which language is selected and then proceeding with taking the input sentence
# only 5 languages are supported as of now
# Spanish, French, Hindi, Arabic, Korean, else it is unsupported

def language(message):
    global selected_language_code
    selected_language_code = message.text
    lower_code = selected_language_code.casefold()

    if lower_code in ['es', 'fr', 'hi', 'ar', 'ko']:
        selected_language_name = lang_codes.get(lower_code)
        bot.send_message(message.chat.id, " Type in the English sentence you want to translate to " + selected_language_name)
        bot.register_next_step_handler(message, translation_process)
    else:
        bot.reply_to(message, "Unsupported or wrong language code")
    return lower_code


# Translation process happens in this code block
# using the microsoft translator api to translate the text input by the user
# api key for microsoft translator can be found in the Azure portal on the Keys and Endpoint page.

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
        'to': selected_language_code
    }

    headers = {
        'Ocp-Apim-Subscription-Key': mst_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

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