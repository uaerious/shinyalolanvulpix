from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = Updater(token='1770413790:AAHzEfkjLUlcq2OH5cAAml_AWV7-t9gir6A', use_context=True)

# commands

def start(update, context):
    update.message.reply_text(f'Welcome to this bot\n'
                              f'/help for assistance 😉\n\n'
                              f'A wild Error 2 appeared! /error')


def error(update, context):
    update.message.reply_text(f'This are current errors :o\n\n'
                              f'Error list:\n\n'
                              f'Error 1: Not a valid command\n'
                              f'Error 2: Currently under maintenance /downtime'
                              )


def help(update, context):
    update.message.reply_text(f'help list is currently not available...\n'
                              f'during downtime echo is ON by default\n'
                              f"can't turn it off sorry...\n"
                              f'/downtime')


def echo(update, context):
    update.message.reply_text(text='/downtime')


def downtime(update, context):
    update.message.reply_text(f'estimated 1 hour update sorryyyy :(\n'
                              f'give it a break :D')

# dispatcher
dp = updater.dispatcher

dp.add_handler(CommandHandler('start', start))
dp.add_handler(CommandHandler('error', error))
dp.add_handler(CommandHandler('help', help))
dp.add_handler(CommandHandler('downtime', downtime))
dp.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))

# other commands

def unknown(update, context):
    update.message.reply_text(f"What's this?\n"
                              f"A wild Error 2 appeared!\n"
                              f"/error for more details :D")

dp.add_handler(MessageHandler(Filters.command, unknown))

# waiting for commands from user
updater.start_polling()
