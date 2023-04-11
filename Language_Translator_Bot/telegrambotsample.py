import os
import telebot

#Store the API token key in a txt file and read it in the code

with open("token_file.txt",'r') as f:
    API_KEY = f.readline()

#Create the bot
bot = telebot.TeleBot(API_KEY)

#start sending messages

# hello command
@bot.message_handler(commands=['hello'])
def hello(message):
    bot.send_message(message.chat.id,"Hi, I am the Translation Express Bot!\n"
                                     "How can I help you today?")


#start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,"Hey, hows it going")

bot.polling()