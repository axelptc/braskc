from typing import Tuple
from telegram import*
from telegram.ext import*
from datetime import*
from pytz import timezone

def sondage(context:CallbackContext):
    options = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche','Pas là', 'Sydney Govou']
    bot.send_poll(-1001165380533, 'Five cette semaine', options, False, allows_multiple_answers=True )

updater = Updater('5672453377:AAER_0xzOwUs8hVcKyEb_l-xcte6Y_16oVg', use_context=True)
bot = updater.bot
j = updater.job_queue
j.run_repeating(sondage, timedelta(days=7), first=datetime(2022,10,9,14,0,0))
updater.start_polling()
updater.idle()
