from telegram import Update 
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import yaml
from yaml.loader import SafeLoader


with open('../config/settings.yaml', 'r',  encoding="UTF-8") as file:
    data = yaml.load(file, Loader=SafeLoader)


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: 
    await update.message.reply_text('Hello')

app = ApplicationBuilder().token(data["token"]).build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()
