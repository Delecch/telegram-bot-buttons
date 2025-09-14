# telegram-bot-buttons

FastAPI + python-telegram-bot webhook implementation with inline keyboard buttons for Support and Website links.

## Features

- FastAPI webhook endpoint for Telegram bot
- `/start` command with inline keyboard
- Two buttons: "Support" (https://t.me/crescitaly) and "Website" (https://crescitaly.com)
- Health check endpoint
- Railway deployment ready

## Environment Variables

Set the following environment variables:

```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
RAILWAY_PUBLIC_DOMAIN=your-app-name.railway.app
```

## Local Development

```bash
pip install -r requirements.txt
python main.py
```

## Railway Deployment

Add this start command in Railway:

```
hypercorn main:app --bind "[::]:$PORT"
```

## Webhook Setup

After deployment, set your Telegram webhook URL to:
```
https://your-domain.railway.app/
```

## Files

- `main.py` - FastAPI application with webhook handler
- `requirements.txt` - Python dependencies
- `README.md` - This documentation
