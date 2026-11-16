import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

def menu():
    keyboard = [
        [InlineKeyboardButton("⚡ Електроопалення", callback_data="heating")],
        [InlineKeyboardButton("☀️ Сонячні електростанції", callback_data="solar")],
        [InlineKeyboardButton("♨️ Тепла підлога", callback_data="floor")],
        [InlineKeyboardButton("🏠 Про компанію", callback_data="about")],
        [InlineKeyboardButton("📞 Контакти", callback_data="contacts")],
        [InlineKeyboardButton("🌐 Наш сайт", url="https://smartopalennya.com.ua/")]
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Вітаємо! Оберіть, що вас цікавить 👇",
        reply_markup=menu()
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    texts = {
        "heating": "⚡ Електроопалення\nСучасні рішення для опалення вашого приміщення.",
        "solar": "☀️ Сонячні електростанції\nРішення для використання сонячної енергії.",
        "floor": "♨️ Тепла підлога\nКомфортне опалення для вашої оселі.",
        "about": "🏠 Smart Opalennya\nДетальніше про послуги та компанію — на нашому сайті.",
        "contacts": "📞 Наші контакти:\n+380 99 681 78 08\n+380 96 950 34 35"
    }

    await query.edit_message_text(
        texts.get(query.data, "Оберіть розділ."),
        reply_markup=menu()
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))
app.run_polling()
