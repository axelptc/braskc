from typing import Tuple
from telegram import*
from telegram.ext import*
from datetime import*
from pytz import timezone

def sondage(context:CallbackContext):
    options = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche','Pas là', 'Sidney Govou']
    sondage = bot.send_poll(-1001165380533, 'Five cette semaine', options, False, allows_multiple_answers=True )
    bot.forward_message(-1001534868512, -1001165380533, sondage.message_id)

def heure(context:CallbackContext):
    options = ['10h', '11h', '12h', '13h', '14h', '15h', '16h','17h', 'Sidney Govou']
    sondage = bot.send_poll(-1001165380533, 'Horaire Samedi', options, False, allows_multiple_answers=True )
    bot.forward_message(-1001534868512, -1001165380533, sondage.message_id)

updater = Updater('5672453377:AAER_0xzOwUs8hVcKyEb_l-xcte6Y_16oVg', use_context=True)
bot = updater.bot
j = updater.job_queue
j.run_repeating(sondage, timedelta(days=7), first=datetime(2022,10,9,14,0,0))
j.run_repeating(heure, timedelta(days=7), first=datetime(2022,10,12,16,0,0))
j.run_repeating(heure, timedelta(days=7), first=datetime(2022,10,8,7,0,0))
updater.start_polling()
updater.idle()
