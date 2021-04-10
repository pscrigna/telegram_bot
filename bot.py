from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from decouple import config


# Define a few command handlers.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text(f'Hola {update.message.from_user.first_name}')
    print(update)


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Necesitas ayuda?')


def promo(update, context):
    """Send a message when the command /promo is issued. """
    update.message.reply_text('Las promos del dia son')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    TOKEN = config("TOKEN")
    print(TOKEN)
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("promo", promo))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
