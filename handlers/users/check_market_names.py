from aiogram import types
from loader import dp
from keyboards.default.keyboards import keyboard_reklama, keyboard_sahna, keyboard_start, keyboard_Yozuvli
from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes

rasmlar = {
    "Sahna": ["images/2.jpg"],
    "Salyut": ["images/1.jpg"],
    "Dim uskuna": ["images/3.jpg"],
    "Yo'lak": ["images/1.jpg"],
    "Tashqi bezak": ["images/2.jpg"],
    "Ichki bezak": ["images/3.jpg"],
    "Onajon": ["images/1.jpg"],
    "Dadajon": ["images/1.jpg"],
    "Kalonkalar Ijroga": ["images/1.jpg"],
    "Banner": ["images/1.jpg"],
    "Arakal": ["images/1.jpg"],
    "Setka": ["images/1.jpg"],
    "3D Harflar": ["images/1.jpg"],
    "Flayerlar va Vizitkalar": ["images/1.jpg"],
    "AVTO uchun reklamalar": ["images/1.jpg"],
    "Boshqa Xizmatlar": ["images/1.jpg"],
}

key = rasmlar.keys()
print(key)

@dp.callback_query_handler(lambda x: x.data in key)
async def qwer(message: types.CallbackQuery):
    print(rasmlar[message.data], "hi")
    await dp.bot.send_photo(message.message.chat.id, photo=open(f"{rasmlar[message.data][0]}", "rb"))


@dp.message_handler(commands=['id'])
async def group_id(message: types.Message):
    await message.answer(text= f"channel_id: {message.chat.id}")

@dp.callback_query_handler(lambda x: x.data == "Sahna Bezaklari")
async def asd(message: types.CallbackQuery):
    await message.message.reply("Kerakli tugmachalar orqali hizmatlardan keraklisini tanlang", reply_markup=keyboard_sahna)


@dp.callback_query_handler(lambda x: x.data == "Yozuvli Tabriklar")
async def dsa(message: types.CallbackQuery):
    await message.message.reply("Kerakli tugmachalar orqali hizmatlardan keraklisini tanlang", reply_markup=keyboard_Yozuvli)


@dp.callback_query_handler(lambda x: x.data == "Reklama, Banner, Hizmatlari")
async def sad(message: types.CallbackQuery):
    await message.message.reply("Kerakli tugmachalar orqali hizmatlardan keraklisini tanlang", reply_markup=keyboard_reklama)

@dp.callback_query_handler(lambda x: x.data == "home")
async def home(message: types.CallbackQuery):
    await message.reply("Assalomu aleykum.\nSiz Koson tumani reklama agentligi botiga tashrif buyurdingiz.\nO'zingizga kerakli bo'limni tanlang.\n\nBizga bog'lanish va yordam uchun /help commandasini yuboring!", reply_markup=keyboard_start)
