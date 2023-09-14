from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard_start = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)

keyboard_start.add(
        InlineKeyboardButton(text="Sahna Bezaklari", callback_data='Sahna Bezaklari'),
        InlineKeyboardButton(text="Yozuvli Tabriklar", callback_data="Yozuvli Tabriklar"),
        InlineKeyboardButton(text="Reklama, Banner, Hizmatlari", callback_data="Reklama, Banner, Hizmatlari"),
        InlineKeyboardButton(text="Biz bilan bog'lanish", callback_data="Biz bilan bog'lanish"),
    
)

keyboard_sahna = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)

keyboard_sahna.add(
        InlineKeyboardButton(text="Sahna", callback_data="Sahna"),
        InlineKeyboardButton(text="Yo'lak", callback_data="Yo'lak"),
        InlineKeyboardButton(text="Salyut", callback_data="Salyut"),
        InlineKeyboardButton(text="Dim uskuna", callback_data="Dim uskuna"),
        InlineKeyboardButton(text="Tashqi bezak", callback_data="Tashqi bezak"),
        InlineKeyboardButton(text="Ichki bezak", callback_data="Ichki bezak"),
        InlineKeyboardButton(text="Sharlar", callback_data="Sharlar"),
)


keyboard_Yozuvli = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

keyboard_Yozuvli.add(
        KeyboardButton(text="Onajon"),
        KeyboardButton(text="Dadajon"),
        KeyboardButton(text="Kalonkalar Ijroga"),
)



keyboard_reklama = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

keyboard_reklama.add(
        KeyboardButton(text="Banner"),
        KeyboardButton(text="Arakal"),
        KeyboardButton(text="Setka"),
        KeyboardButton(text="3D Harflar"),
        KeyboardButton(text="Stentlar"),
        KeyboardButton(text="Flayerlar va Vizitkalar"),
        KeyboardButton(text="AVTO uchun reklamalar"),
        KeyboardButton(text="Boshqa Xizmatlar"),
)