from telegram import*
from telegram.ext import*
from datetime import*
from pytz import timezone

def sondage(context:CallbackContext):
    options = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche','Pas là', 'Sydney Govou']
    bot.send_poll(1953752060, 'Five cette semaine', options, False, allows_multiple_answers=True )


updater = Updater('5672453377:AAG-MbOf4Ni-yIDCYV1he8C0XHlpxMQX7cw', use_context=True)
bot = updater.bot
j = updater.job_queue
j.run_daily(sondage, time=time(11,33,0,0),days=(0,1,2,3,4,5,6))


