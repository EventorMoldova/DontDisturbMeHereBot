from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Configurarea serverului Flask
app = Flask('')

@app.route('/')
def home():
    return "Botul este activ!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Funcțiile pentru bot
async def greet_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Trimitem un mesaj de salut către utilizatorul care a trimis un mesaj
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Salut! Cum pot să te ajut?")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Mesajul trimis când utilizatorul folosește comanda /start
    await update.message.reply_text("Salut! Eu sunt un bot pregătit să răspund.")

if __name__ == "__main__":
    # Creează aplicația botului cu tokenul API de la BotFather
    application = ApplicationBuilder().token("7849522428:AAFKfnqj3We0frTBpVZudMr6kS0rYU0fCso").build()

    # Adaugă handler-ul pentru comanda /start
    application.add_handler(CommandHandler("start", start))

    # Adaugă handler-ul pentru orice mesaj primit
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), greet_user))

    # Pornește serverul Flask
    keep_alive()

    # Rulează botul
    application.run_polling()
