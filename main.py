import random
from datetime import date

today_date = date.today()

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from uuid import uuid4

updater = Updater(token='1770413790:AAHzEfkjLUlcq2OH5cAAml_AWV7-t9gir6A', use_context=True)
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
    update.message.reply_text(f'/start to ensure bot is up to date\n\n'
                              f'/hello for a warm greeting 😃\n\n'
                              f'/feelings to send your feelings 🥰\n\n'
                              f'/error to look at known error list\n\n'
                              f'/recent for recent update notes\n\n'
                              f'/QOTD for quote of the day!\n\n'
                              f'/echooff turns off echo\n\n'
                              f'/echoon turns on echo - currently OFF by default\n'
                              f'go rawr at the bot with echo hehe\n\n'
                              f'/ily the bot suddenly is your other half :o\n\n'
                              f'/downtime shows the downtime/next scheduled update\n\n'
                              f'/version for people who are just curious on such stuff\n\n'
                              f'you could always ask Wayn for help 😉\n'
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
    update.message.reply_text(f'Last update: 7/7/2021\n\n'
                              f'-New commands hehe\n'
                              f'-simpler codes whee\n'
                              f'-echo is OFF by DEFAULT and can be turned ON\n'
                              f'-working hard to bring in InlineKeyboard\n'
                              f'-making the bot more friendly\n'
                              f'-some features work now...\n'
                              f'soon to be in beta...'
                              )


# 7
def secret(update, context):
    update.message.reply_text(f'WOAH!\n'
                              f'https://open.spotify.com/playlist/429y59z0RjyDszbJbGfn7m?si=eb3a48e033504782')


# 8
def QOTD(update, context):
    update.message.reply_text(f'https://www.brainyquote.com/topics/daily-quotes\n'
                              f'is the link ok? or should we just have the quote itself?\n'
                              f'tell wayn hehe i cant collect responses yet D:')


# 9 
def ily(update, context):
    update.message.reply_text(f'ily🥺🥰\n'
                              f'https://www.youtube.com/watch?v=T_VJv_079l8\n\n'
                              f'https://www.youtube.com/watch?v=Gj8sBYRwvI4\n\n'
                              f'https://www.youtube.com/watch?v=zb_IOQhHvsE')


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
    updater = Updater('1770413790:AAHzEfkjLUlcq2OH5cAAml_AWV7-t9gir6A', use_context=True)
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


# 13 downtime
def downtime(update, context):
    update.message.reply_text(f'there is no maintenance currently...\n'
                              f'next scheduled update: NA')


# 14 version
def version(update, context):
    update.message.reply_text(f'CLOSED TESTING ALPHA\n'
                              f'Version: Alpha\n\n'
                              f'check /recent for the latest update')


# 15 april fools stuff
def update_bot(update, context):
    update.message.reply_text(f'HAH U LEGIT THOUGHT THERE WAS?'
                              f'APRIL FOOLS')


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
dispatcher.add_handler(CommandHandler('downtime', downtime))
dispatcher.add_handler(CommandHandler('version', version))
dispatcher.add_handler(CommandHandler('update_bot',update_bot))

# when user sends commands that are not added
def unknown(update, context):
    update.message.reply_text(f"What's this?\n"
                              f"A wild Error 1 appeared!\n"
                              f"/error for more details :D")


dispatcher.add_handler(MessageHandler(Filters.command, unknown))

# waiting for commands from user
updater.start_polling()
