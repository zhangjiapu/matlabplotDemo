from wxpy import *

turing = Tuling(api_key="73524e5012064cc7b176c0c0de417cd3")
bot = Bot()

fireman = bot.friends().search("苏幕遮")

@bot.register(chats=fireman)
def communicate(msg):
    turing.do_reply(msg)

bot.join()