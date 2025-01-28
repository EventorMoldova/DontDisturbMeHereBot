from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, Filters, CallbackContext
from keep_alive import keep_alive

# Tokenul tău de bot Telegram (trebuie să-l înlocuiești cu cel real)
TELEGRAM_TOKEN = "7849522428:AAFKfnqj3We0frTBpVZudMr6kS0rYU0fCso"

# Startul botului
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Salut! Eu sunt un bot care nu folosește Telegram. Cum te pot ajuta?')

# Funcția pentru mesajele primite
async def handle_message(update: Update, context: CallbackContext) -> None:
    if update.message.chat.type == "private":  # Asigură-te că mesajul provine dintr-un chat privat
        await update.message.reply_text('Eu nu folosesc Telegramul, dar pot să-ți răspund!')

# Rularea botului
def main():
    # Crează aplicația botului
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Adaugă handler-ul pentru comanda /start
    application.add_handler(CommandHandler("start", start))
    
    # Adaugă handler-ul pentru mesaje
    application.add_handler(MessageHandler(Filters.all, handle_message))  # Răspunde la orice mesaj

    # Începe botul
    application.run_polling()

# Lansează botul și Flask
if __name__ == "__main__":
    keep_alive()  # Lansează serverul Flask
    main()  # Lansează botul Telegram
