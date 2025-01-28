from keep_alive import keep_alive
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Tokenul tău de bot Telegram (trebuie să-l înlocuiești cu cel real)
TELEGRAM_TOKEN = "7849522428:AAFKfnqj3We0frTBpVZudMr6kS0rYU0fCso"

# Funcția pentru comanda /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Salut! Eu sunt un bot care nu folosește Telegram. Cum te pot ajuta?')

# Rularea botului
def main():
    # Crează aplicația botului
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Adaugă handler-ul pentru comanda /start
    application.add_handler(CommandHandler("start", start))
    
    # Începe botul
    application.run_polling()

# Lansează botul și Flask
if __name__ == "__main__":
    keep_alive()  # Lansează serverul Flask
    main()  # Lansează botul Telegram
