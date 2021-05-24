from datetime import date
today_date = date.today()

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

updater = Updater(token='token', use_context=True)
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# define commands

# 1
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Welcome to this bot!\n'
                                                                    '/help for help :D')

# 2
def error(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Error list:\n\n'
                                                                    'Error 1: Command not created\n\n'
                                                                    'THIS LIST WILL BE UPDATED')

# 3
def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='/hello for daily date\n\n'
                                                                    '/feelings to send your feelings 🥰\n\n'
                                                                    '/error to look at known error list\n\n'
                                                                    '/recent for recent update notes\n\n'
                                                                    '/QOTD for quote of the day!\n\n'
                                                                    'or you could always ask Wayn for help 😉\n\n'
                                                                    'text him to give ur suggestions! :D'
                             )

# 4
def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'Hewo! Today is {today_date}')

# 5
def feelings(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='How are you feeling today?')

# 6
def recent(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Last update: 24/5/2021\n'
                                                                    '-making code simple')

# 7
def secret(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='WOAH!')

# 8
def QOTD(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='quote. CURRENTLY IN DEVELOPMENT THANKS')


# to start the commands with handler and dispatcher

start_handler = CommandHandler('start', start)
error_handler = CommandHandler('error', error)
help_handler = CommandHandler('help', help)
hello_handler = CommandHandler('hello', hello)
feelings_handler = CommandHandler('feelings', feelings)
recent_handler = CommandHandler('recent', recent)
secret_handler = CommandHandler('secret', secret)
QOTD_handler = CommandHandler('QOTD', QOTD)

dispatcher = updater.dispatcher

dispatcher.add_handler(start_handler)
dispatcher.add_handler(error_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(hello_handler)
dispatcher.add_handler(feelings_handler)
dispatcher.add_handler(recent_handler)
dispatcher.add_handler(secret_handler)
dispatcher.add_handler(QOTD_handler)

# when user sends commands that are not added
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="An error occurred. Error 1")


unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

# waiting for commands from user
updater.start_polling()
