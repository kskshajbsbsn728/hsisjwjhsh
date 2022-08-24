from telegram.ext import *

def wm(u,c):
    u.message.reply_text(u.message.text)
    

upd = Updater("5691804740:AAFOJtZTvnpaVYrvtOwfVTWUx1-jSTu0hUM",use_context=True)
upd.dispatcher.add_handler("start",wm)

upd.start_polling()
upd.idle()
