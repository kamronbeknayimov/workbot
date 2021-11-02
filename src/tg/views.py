from django.shortcuts import render


# Create your views here.


def start(update, context):
    update.message.reply_text("salom dunyo")
