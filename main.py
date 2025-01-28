from keep_alive import keep_alive
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext

# Tokenul tău de bot Telegram (trebuie să-l înlocuiești cu cel real)
TELEGRAM_TOKEN = "7849522428:AAFKfnqj3We0frTBpVZudMr6kS0rYU0fCso"

# Funcția care răspunde la orice mesaj privat
async def handle_message(update: Update, context: CallbackContext) -> None:
    # Verifică dacă mesajul provine dintr-un chat privat
    if update.message.chat.type == "private":
        # Răspunde în chatul privat cu mesajul dorit
        await update.message.reply_text('Eu nu folosesc Telegramul, dar pot să-ți răspund!')

# Rularea botului
def main():
    # Crează aplicația botului
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Adaugă handler-ul pentru mesaje (orice tip de mesaj, filtrat doar pentru mesaje private)
    application.add_handler(MessageHandler(filters.TEXT & filters.Private, handle_message))  # Răspunde doar la mesaje private

    # Începe botul
    application.run_polling()

# Lansează botul și Flask
if __name__ == "__main__":
    keep_alive()  # Lansează serverul Flask
    main()  # Lansează botul Telegram
