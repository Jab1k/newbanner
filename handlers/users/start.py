from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ContentType
from loader import dp
from keyboards.default.keyboards import *
import datetime


@dp.message_handler(content_types=ContentType.ANY, chat_type=['private'], commands=["start", "help"])
async def welcome(message: types.Message):
   print("privet")
   await message.reply("Assalomu aleykum.\nSiz Koson tumani reklama agentligi botiga tashrif buyurdingiz.\nO'zingizga kerakli bo'limni tanlang.\n\nBizga bog'lanish va yordam uchun /help commandasini yuboring!", reply_markup=keyboard_start)
#    await dp.bot.send_message(-1001852245312, text=f"""
# Idsi: {message.from_user.id}
# 👤Ismi: {message.from_user.full_name}
# ℹ️username: @{message.from_user.username}
# 🕛vaqt: {datetime.datetime.now()}
# ✍️Nima dep yozdi: {message.text}
#        """)

