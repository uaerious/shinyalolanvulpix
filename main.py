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
    # echo off by default; sends alot of internal error
    update.message.reply_text(f'Welcome to this bot\n'
                              f'/help for assistance 😉')


# 2
def error(update, context):
    update.message.reply_text(f'This are current errors :o\n\n'
                              f'Error list:\n\n'
                              f'Error 1: Not a valid command\n'
                              f'Error 2: Currently under maintenance...'
                              )


# 3
def help(update, context):
    update.message.reply_text(f'/start to ensure bot is up to date\n\n'
                              f'/hello for a warm greeting 😃\n\n'
                              f'/feelings to send your feelings 🥰\n\n'
                              f'/goodmorning :D morning!\n\n'
                              f'/goodnight D: goodnight!\n\n'
                              f'/error to look at known error list\n\n'
                              f'/recent for recent update notes\n\n'
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
    update.message.reply_text(f'How are you feeling today?')  # need inlinekeyboardMarkup


# 6
def recent(update, context):
    update.message.reply_text(f'Last update: 19/7/2021\n\n'
                              f'-working hard to bring in InlineKeyboard\n'
                              f'-removed QOTD as I cant find a QOTD website :(\n'
                              f'good morning! or good night! 😉'
                              )


# 7
def secret(update, context):
    update.message.reply_text(f'WOAH!\n'
                              f'https://open.spotify.com/playlist/429y59z0RjyDszbJbGfn7m?si=eb3a48e033504782\n\n'
                              f'https://open.spotify.com/track/50BmNitVXwo8yi2VieV1ME?si=6b694677609d433d')

# 8
def ily(update, context):
    update.message.reply_text(f'ily🥺🥰\n'
                              f'https://www.youtube.com/watch?v=T_VJv_079l8\n\n'
                              f'https://www.youtube.com/watch?v=Gj8sBYRwvI4\n\n'
                              f'https://www.youtube.com/watch?v=zb_IOQhHvsE')


# 9 InlineKeyboard set status?
def status(update, context):
    update.message.reply_text(f'ight what now')


# 10 very lengthy echo setup :rolleye:

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

# 11
def downtime(update, context):
    update.message.reply_text(f'there is no maintenance currently...\n'
                              f'next scheduled update: NA')


# 12
def version(update, context):
    update.message.reply_text(f'OPEN TESTING ALPHA\n'
                              f'Version: Alpha\n\n'
                              f'check /recent for the latest update')


# 13
def goodmorning(update, context):
    update.message.reply_text(f'good morning,{update.effective_user.first_name}! 🥺')


# 14
def goodnight(update, context):
    update.message.reply_text(f'good night,{update.effective_user.first_name}! 🥺\n'
                              f'time for me to sleep toooo...')


# 15 april fools stuff
def update_bot(update, context):
    update.message.reply_text(f'HAH U LEGIT THOUGHT THERE WAS?\n'
                              f'APRIL FOOLS!')


# to start the commands with handler and dispatcher

dp = updater.dispatcher

dp.add_handler(CommandHandler('start', start))
dp.add_handler(CommandHandler('error', error))
dp.add_handler(CommandHandler('help', help))
dp.add_handler(CommandHandler('hello', hello))
dp.add_handler(CommandHandler('feelings', feelings))
dp.add_handler(CommandHandler('recent', recent))
dp.add_handler(CommandHandler('secret', secret))
dp.add_handler(CommandHandler('ily', ily))
dp.add_handler(CommandHandler('status', status))
dp.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))
dp.add_handler(CommandHandler('echooff', echooff))
dp.add_handler(CommandHandler('echoon', echoon))
dp.add_handler(CommandHandler('downtime', downtime))
dp.add_handler(CommandHandler('version', version))
dp.add_handler(CommandHandler('goodmorning', goodmorning))
dp.add_handler(CommandHandler('goodnight', goodnight))
dp.add_handler(CommandHandler('update_bot',update_bot))


# when user sends commands that are not added
def unknown(update, context):
    update.message.reply_text(f"What's this?\n"
                              f"A wild Error 1 appeared!\n"
                              f"/error for more details :D")


dp.add_handler(MessageHandler(Filters.command, unknown))

# waiting for commands from user
updater.start_polling()
