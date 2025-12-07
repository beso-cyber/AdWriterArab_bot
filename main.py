from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN, ADMIN_ID
from bot.handlers import register_handlers
from web.server import start_webhook

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

register_handlers(dp)

if __name__ == "__main__":
    start_webhook()
    executor.start_polling(dp, skip_updates=True)
