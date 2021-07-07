import random
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
                              f'/echoON turns on echo - currently OFF by default\n'
                              f'go rawr at the bot with echo hehe\n\n'
                              f'/ily the bot suddenly is your other half :o\n\n'
                              f'or you could always ask Wayn for help 😉\n\n'
                              f'text him to give ur suggestions! :D\n'
                              f'go explore the hidden commands hehe'
                              )


# 4
def hello(update, context) -> None:
    update.message.reply_text(f'Hiii {update.effective_user.first_name}👋, today is {today_date}')


# 5
def feelings(update, context):
    update.message.reply_text(f'How are you feeling today?')  # need ReplyKeyboardMarkup


# 6
def recent(update, context):
    update.message.reply_text(f'Last update: 7/7/2021\n'
                              f'-New commands hehe\n'
                              f'-simpler codes whee\n'
                              f'-echo is OFF by DEFAULT and can be turned ON\n'
                              f'-working hard to bring in InlineKeyboard\n'
                              f'making the bot more friendly\n'
                              f'-eliminating bugs'
                              f'soon to be in beta'
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


# 10 InlineKeyboard set status?
def status(update, context):
    update.message.reply_text(f'ight what now')


# 11 very lengthy echo setup :rolleye:

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


def echoon(update, context):
    context.user_data['is_echo'] = True
    update.message.reply_text(f'echo is on...')


def echooff(update, context):
    context.user_data['is_echo'] = False
    update.message.reply_text(f'turned off now...')


# 12 inlinekeyboard for the user to pick a choice
def sps(update, context):
    possible_actions = ['scissors', 'paper', 'stone']
    computer_action = random.choice(possible_actions)
    user_choice = ['scissors', 'paper', 'stone']
    update.message.reply_text(f'I chose {computer_action}, you chose {user_choice}!')


# 13 april fools stuff

# to start the commands with handler and dispatcher

dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('error', error))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('hello', hello))
dispatcher.add_handler(CommandHandler('feelings', feelings))
dispatcher.add_handler(CommandHandler('recent', recent))
dispatcher.add_handler(CommandHandler('secret', secret))
dispatcher.add_handler(CommandHandler('QOTD', QOTD))
dispatcher.add_handler(CommandHandler('ily', ily))
dispatcher.add_handler(CommandHandler('status', status))
dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))
dispatcher.add_handler(CommandHandler('echooff', echooff))
dispatcher.add_handler(CommandHandler('echoon', echoon))


# when user sends commands that are not added
def unknown(update, context):
    update.message.reply_text(f"What's this?\n"
                              f"A wild Error 1 appeared!\n"
                              f"/error for more details :D")


dispatcher.add_handler(MessageHandler(Filters.command, unknown))

# waiting for commands from user
updater.start_polling()
