from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import time
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = Updater(token='token', use_context=True)

# commands

def start(update, context):
    update.message.reply_text(f'Welcome to this bot')
    time.sleep(0.1)
    update.message.reply_text(f'/help for assistance 😉')
    time.sleep(0.2)
    update.message.reply_text(f'A wild Error 2 appeared! /error')


def error(update, context):
    update.message.reply_text(f'This are current errors :o\n\n'
                              f'Error list:\n\n'
                              f'Error 1: Not a valid command\n'
                              f'Error 2: Currently under maintenance /downtime'
                              )

def help(update,context):
    update.message.reply_text(f'Help list is unavailable while down :(')

def echo(update, context):
    update.message.reply_text(text='/downtime')


def downtime(update, context):
    update.message.reply_text(f'estimated 1 hour update sorryyyy :(')
    time.sleep(0.4)
    update.message.reply_text(f'give it a break :D')

# dispatcher
dp = updater.dispatcher

dp.add_handler(CommandHandler('start', start))
dp.add_handler(CommandHandler('error', error))
dp.add_handler(CommandHandler('help', help))
dp.add_handler(CommandHandler('downtime', downtime))
dp.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))

# other commands

def unknown(update, context):
    update.message.reply_text(f"What's this?")
    time.sleep(0.2)
    update.message.reply_text(f"A wild Error 2 appeared!")
    time.sleep(0.3)
    update.message.reply_text(f"/error for more details :D")

dp.add_handler(MessageHandler(Filters.command, unknown))

# waiting for commands from user
updater.start_polling()
