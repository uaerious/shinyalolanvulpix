from datetime import date

today_date = date.today()

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from uuid import uuid4

updater = Updater(token='TOKEN', use_context=True)
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


# define commands

# 1
def start(update, context):
    # echo off by default
    update.message.reply_text(f'Welcome to this bot\n'
                              f'/help for assistance 😉')

# 2
def error(update, context):
    update.message.reply_text(f'This are current errors :o\n\n'
                              f'Error list:\n\n'
                              f'Error 1: Not a valid command\n'
                              f'Error 2: Currently under maintenance'
                              )


# 3
def help(update, context):
    update.message.reply_text(f'/hello for daily date\n\n'
                              f'/feelings to send your feelings 🥰\n\n'
                              f'/error to look at known error list\n\n'
                              f'/recent for recent update notes\n\n'
                              f'/QOTD for quote of the day!\n\n'
                              f'/echoOFF turns off echo\n\n'
                              f'/echoON turns on echo - currently OFF by default\n\n'
                              f'or you could always ask Wayn for help 😉\n\n'
                              f'text him to give ur suggestions! :D\n'
                              f'go explore the hidden commands hehe'
                             )


# 4
def hello(update, context)-> None:
    update.message.reply_text(f'Hewo {update.effective_user.first_name}, today is {today_date}')


# 5
def feelings(update, context):
    update.message.reply_text(f'How are you feeling today?')  # need ReplyKeyboardMarkup


# 6
def recent(update, context):
    update.message.reply_text(f'Last update: 6/7/2021\n'
                              f'-New commands hehe\n\n'
                              f'simpler codes whee\n\n'
                              f'echo is OFF by DEFAULT and can be turned ON\n'
                              f'working hard to bring in InlineKeyboard'
                             )

# 7
def secret(update, context):  # need ReplyKeyboardMarkup, inline mode to place the spotify link?
    update.message.reply_text(f'WOAH!')


# 8
def QOTD(update, context):  # inline mode? provide link to external website?
    update.message.reply_text(f'quote. CURRENTLY IN DEVELOPMENT THANKS')


# 9
def ily(update, context):
    update.message.reply_text(f'ily🥺🥰')


# 10 for another future command use
def newcommand(update, context):
    update.message.reply_text(f'meow')

#11 very lengthy echo setup :rolleye:

def put(update, context):
    """Usage: /put value"""
    # Generate ID and separate value from command
    key = str(uuid4())
    # We don't use context.args here, because the value may contain whitespaces
    is_echo = update.message.text.partition(' ')[2]

    # Store value
    context.user_data[key] = is_echo
    # Send the key to the user
    update.message.reply_text(key)

def get(update, context):
    """Usage: /get uuid"""
    # Seperate ID from command
    key = context.args[0]

    # Load value and send it to the user
    is_echo = context.user_data.get(key, 'is_echo')
    update.message.reply_text(is_echo)

if __name__ == '__main__':
    updater = Updater('TOKEN', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('put', put))
    dp.add_handler(CommandHandler('get', get))

def echo(update, context):
    if context.user_data['is_echo']:
       update.message.reply_text(update.message.text)
    else:
        print('echo off')

def echoON(update, context):
    context.user_data['is_echo'] = True
    update.message.reply_text(f'echo is on...')

def echoOFF(update, context):
    context.user_data['is_echo'] = False
    update.message.reply_text(f'turned off now...')


# to start the commands with handler and dispatcher

start_handler = CommandHandler('start', start)
error_handler = CommandHandler('error', error)
help_handler = CommandHandler('help', help)
hello_handler = CommandHandler('hello', hello)
feelings_handler = CommandHandler('feelings', feelings)
recent_handler = CommandHandler('recent', recent)
secret_handler = CommandHandler('secret', secret)
QOTD_handler = CommandHandler('QOTD', QOTD)
ily_handler = CommandHandler('ily', ily)
newcommand_handler = CommandHandler('newcommand', newcommand)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

dispatcher = updater.dispatcher

dispatcher.add_handler(start_handler)
dispatcher.add_handler(error_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(hello_handler)
dispatcher.add_handler(feelings_handler)
dispatcher.add_handler(recent_handler)
dispatcher.add_handler(secret_handler)
dispatcher.add_handler(QOTD_handler)
dispatcher.add_handler(ily_handler)
dispatcher.add_handler(newcommand_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(CommandHandler('echoOFF', echoOFF))
dispatcher.add_handler(CommandHandler('echoON', echoON))


# when user sends commands that are not added
def unknown(update, context):
    update.message.reply_text(f"What's this?\n"
                              f"A wild Error 1 appeared!\n"
                              f"/error for more details :D")


unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

# waiting for commands from user
updater.start_polling()
