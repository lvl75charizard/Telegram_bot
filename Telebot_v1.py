import telebot
import key as k
import freeGames as FG
# I add the epic reminder as a part of the both
bot = telebot.TeleBot(k.API_Key)


# All commands in the telegram app must be entered like this with a forward slash and then the command eg. /greet
@bot.message_handler(commands=['greet', "greetings"])
def greet(message):
    bot.reply_to(message, "Hello human how make I serve you today?")


# Commands
@bot.message_handler(commands=['help'])
def greet(message):
    bot.reply_to(message, "There isn't much I can right now")


@bot.message_handler(commands=['download'])
def greet(message):
    bot.reply_to(message, "Please submit a link")


@bot.message_handler(commands=['trick'])
def greets(message):
    bot.send_dice(message.chat.id)


# This is identifying specific messages to respond to using regex
@bot.message_handler(regexp="hello")
def handle_message(message):
    bot.send_message(message.chat.id, "Hello! Are you having a wonderful day?")


# This is identifying specific messages to respond to using the epic scrapper to get the free games
@bot.message_handler(regexp="game ")
def handle_message(message):
    bot.send_message(message.chat.id, FG.GetFreeGames()[0] + ' ' + FG.GetFreeGames()[1] + ' \n' + FG.GetFreeGames()[2] + ' ' + FG.GetFreeGames()[3])


# this grabs a specified video and sends it to the user when the regex is satisfied
# @bot.message_handler(regexp="video ")
# def handle_message(message):
#     bot.send_message(message.chat.id, "Here is your video")
#     video = open('ice.mp4', 'rb')
#     bot.send_video(message.chat.id, video)
#     bot.send_message(message.chat_id, "ice")


# This waits for a response from the user at all times
bot.infinity_polling()
