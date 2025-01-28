from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Configurarea serverului Flask
app = Flask('')

@app.route('/')
def home():
    return "1Botul este activ!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Funcția care răspunde automat utilizatorilor
async def greet_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Logăm mesajul primit pentru depanare
    print(f"Am primit un mesaj de la @{update.effective_user.username} (ID: {update.effective_user.id}): {update.message.text}")
    
    # Botul răspunde doar în chaturi private și doar utilizatorilor reali
    if update.effective_chat.type == "private" and not update.effective_user.is_bot:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Salut! Cum pot să te ajut?")

if __name__ == "__main__":
    # Inițializare bot cu tokenul de la BotFather
    application = ApplicationBuilder().token("7849522428:AAFKfnqj3We0frTBpVZudMr6kS0rYU0fCso").build()

    # Adăugăm handler-ul pentru orice mesaj text
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), greet_user))

    # Pornim serverul Flask
    keep_alive()

    # Pornim botul
    application.run_polling()
