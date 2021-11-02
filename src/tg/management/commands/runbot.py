from django.core.management import BaseCommand
from telegram.ext import Updater, CommandHandler

from src.settings import TOKEN
from tg.views import *


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        updater = Updater(TOKEN, use_context=True)
        updater.dispatcher.add_handler(CommandHandler("start", start))

        updater.start_polling()
        updater.idle()
