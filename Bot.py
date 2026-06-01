from telegram.ext import Application, CommandHandler, MessageHandler, filters
import json

# قراءة المعلومات من الملف
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

TOKEN = "8833830244:AAGmxMTXNNn5z8gxUDHe_WuB3ODzFXUdmgYb"

async def start(update, context):
    await update.message.reply_text(
        f"أهلاً! 👋 أنا بوت {config['اسم_المحل']}\n"
        "اكتب /help عشان تعرف أقدر أساعدك بإيه"
    )

async def help_command(update, context):
    await update.message.reply_text(
        "أقدر أساعدك بـ:\n"
        "• مواعيد العمل\n"
        "• الأسعار\n"
        "• الموقع\n"
        "• التواصل معنا"
    )

async def رد_على_الرسايل(update, context):
    رسالة = update.message.text

    if "مواعيد" in رسالة:
        await update.message.reply_text(f"مواعيد العمل: {config['مواعيد_العمل']} 🕙")

    elif "سعر" in رسالة or "أسعار" in رسالة:
        منتجات = "\n".join([f"• {p['اسم']}: {p['سعر']}" for p in config['المنتجات']])
        await update.message.reply_text(f"الأسعار:\n{منتجات}")

    elif "موقع" in رسالة or "فين" in رسالة:
        await update.message.reply_text(f"موقعنا: {config['الموقع']} 📍")

    elif "تواصل" in رسالة or "تليفون" in رسالة:
        await update.message.reply_text(f"تواصل معنا: {config['رقم_التواصل']} 📞")

    else:
        await update.message.reply_text("مش فاهم سؤالك، كتب /help 😊")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(MessageHandler(filters.TEXT, رد_على_الرسايل))

print("البوت شغال! ✅")
app.run_polling()