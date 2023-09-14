from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard_start = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)

keyboard_start.add(
        InlineKeyboardButton(text="Sahna Bezaklari", callback_data='Sahna Bezaklari'),
        InlineKeyboardButton(text="Yozuvli Tabriklar", callback_data="Yozuvli Tabriklar"),
        InlineKeyboardButton(text="Reklama, Banner, Hizmatlari", callback_data="Reklama, Banner, Hizmatlari"),
        InlineKeyboardButton(text="Biz bilan bog'lanish", callback_data="Biz bilan bog'lanish"),
        InlineKeyboardButton(text="Bosh Menyu", callback_data="home"),
    
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
        InlineKeyboardButton(text="Bosh Menyu", callback_data="home"),

)


keyboard_Yozuvli = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)

keyboard_Yozuvli.add(
        InlineKeyboardButton(text="Onajon", callback_data="Onajon"),
        InlineKeyboardButton(text="Dadajon", callback_data="Dadajon"),
        InlineKeyboardButton(text="Kalonkalar Ijaraga", callback_data="Kalonkalar Ijaraga"),
        InlineKeyboardButton(text="Bosh Menyu", callback_data="home"),
)



keyboard_reklama = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)

keyboard_reklama.add(
        InlineKeyboardButton(text="Banner", callback_data="Banner"),
        InlineKeyboardButton(text="Arakal", callback_data="Arakal"),
        InlineKeyboardButton(text="Setka", callback_data="Setka"),
        InlineKeyboardButton(text="3D Harflar", callback_data="3D Harflar"),
        InlineKeyboardButton(text="Stentlar", callback_data="Stentlar"),
        InlineKeyboardButton(text="Flayerlar va Vizitkalar", callback_data="Flayerlar va Vizitkalar"),
        InlineKeyboardButton(text="AVTO uchun reklamalar", callback_data="AVTO uchun reklamalar"),
        InlineKeyboardButton(text="Boshqa Xizmatlar", callback_data="Boshqa Xizmatlar"),
        InlineKeyboardButton(text="Bosh Menyu", callback_data="home"),
)