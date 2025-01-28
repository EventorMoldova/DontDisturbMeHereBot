from keep_alive import keep_alive
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Tokenul tău de bot Telegram (trebuie să-l înlocuiești cu cel real)
TELEGRAM_TOKEN = "7849522428:AAFKfnqj3We0frTBpVZudMr6kS0rYU0fCso"

# Startul botului
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Salut! Eu sunt un bot care nu folosește Telegram. Cum te pot ajuta?')

# Funcția pentru mesajele primite
def handle_message(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Eu nu folosesc Telegramul, dar pot să-ți răspund!')

# Rularea botului
def main():
    # Crează updater-ul și dispatcher-ul
    updater = Updater(TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher
    
    # Adaugă handler-ul pentru comanda /start
    dispatcher.add_handler(CommandHandler("start", start))
    
    # Adaugă handler-ul pentru mesaje
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    
    # Începe botul
    updater.start_polling()

# Lansează botul și Flask
if __name__ == "__main__":
    keep_alive()  # Lansează serverul Flask
    main()  # Lansează botul Telegram
