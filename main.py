import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from company import company_handler
from performer import performer_handler

load_dotenv()  # Load environment variables from .env file

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Create inline buttons for the options
    keyboard = [
        [InlineKeyboardButton("Company", callback_data="button_a")],
        [InlineKeyboardButton("Performer", callback_data="button_b")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Choose an option:", reply_markup=reply_markup)

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Handle the button click event
    query = update.callback_query
    await query.answer()  # Acknowledge the callback query
    if query.data == "button_a":
        await company_handler(update, context)
    elif query.data == "button_b":
        await performer_handler(update, context)

# Read the bot token from environment variable
TOKEN = os.getenv("pliz_bot_token")
app = ApplicationBuilder().token(TOKEN).build()

# Add handlers for commands and callback queries
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_click))

app.run_polling()
