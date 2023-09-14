import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from transliterate import translit

from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message()
async def command_translit(message: Message) -> None:
    start_text = message.text
    new_text = translit(start_text, language_code='ru', reversed=True) 
    await message.reply(new_text)

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
