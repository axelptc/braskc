from typing import Tuple
from telegram import*
from telegram.ext import*
from datetime import*
from pytz import timezone

def sondage(context:CallbackContext):
    options = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche','Pas là', 'Sydney Govou']
    bot.send_poll(1953752060, 'Five cette semaine', options, False, allows_multiple_answers=True )

def job(update,context):
    j = updater.job_queue
    j.run_daily(sondage, time(13,28,0))

updater = Updater('5672453377:AAER_0xzOwUs8hVcKyEb_l-xcte6Y_16oVg', use_context=True)
bot = updater.bot
updater.dispatcher.add_handler(MessageHandler(Filters.update, job, pass_job_queue=True))
updater.start_polling()


