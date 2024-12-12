import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from company import company_handler
from performer import performer_handler

load_dotenv()


async def start(update: Update):
    keyboard = [
        [InlineKeyboardButton("Company", callback_data="button_a")],
        [InlineKeyboardButton("Performer", callback_data="button_b")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Choose an option:", reply_markup=reply_markup)

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "button_a":
        await company_handler(update)
    elif query.data == "button_b":
        await performer_handler(update)

TOKEN = os.getenv("pliz_bot_token")
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_click))

app.run_polling()
