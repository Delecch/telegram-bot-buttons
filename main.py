import os
from fastapi import FastAPI, Request
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Environment variables
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
RAILWAY_PUBLIC_DOMAIN = os.getenv("RAILWAY_PUBLIC_DOMAIN")

# Initialize bot
bot = Bot(token=TELEGRAM_BOT_TOKEN)
application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

async def start_command(update: Update, context):
    """Handle /start command with inline keyboard"""
    keyboard = [
        [
            InlineKeyboardButton("Support", url="https://t.me/crescitaly"),
            InlineKeyboardButton("Website", url="https://crescitaly.com")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Welcome! Choose an option:",
        reply_markup=reply_markup
    )

# Add command handler
application.add_handler(CommandHandler("start", start_command))

@app.post("/")
async def webhook(request: Request):
    """Webhook endpoint for Telegram updates"""
    json_data = await request.json()
    update = Update.de_json(json_data, bot)
    await application.process_update(update)
    return {"status": "ok"}

@app.get("/")
async def health_check():
    """Health check endpoint"""
    return {"status": "Bot is running"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
