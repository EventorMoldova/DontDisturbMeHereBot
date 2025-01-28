sys.version
from telegram import Update
from telegram.ext import Updater, CommandHandler
from keep_alive import keep_alive

def start(update: Update, context):
    update.message.reply_text("Salut! Sunt un bot activ!")

def main():
    updater = Updater("7849522428:AAFKfnqj3We0frTBpVZudMr6kS0rYU0fCso", use_context=True)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()

if __name__ == "__main__":
    keep_alive()
    main()
