from telegram import Update, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def performer_handler(update: Update):
    keyboard = []
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.edit_text("Welcome to the performer section!", reply_markup=reply_markup)
