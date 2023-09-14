from aiogram import types

from loader import dp
import datetime
from aiogram.types import ContentTypes


# Echo bot
@dp.message_handler(content_types=ContentTypes.ANY, chat_type=['private'])
async def bot_echo(message: types.Message):
    print(message.content_type)
    await message.answer("Sizga qanday yordam bera olamiz ?\nMurojaat uchun:\nBizga bog\'laning:\n☎️+998996658666\n☎️+998906088666\n👉@jajikservis👈\nIshlatishni bilmasangiz /help yoki /start commandasini yuboring!\n\nPowered By @JabikJan\n")
    if message.content_type == "text":
        print('text')
        await dp.bot.send_message(chat_id=-1001852245312, text=f"""
Idsi: {message.chat.id}
👤Ismi: {message.from_user.full_name}
ℹ️username: @{message.from_user.username}
🕛vaqt: {datetime.datetime.now()}
✍️Nima dep yozdi yoki nima tashadi: {message.text, message.content_type}
""")
    else:
        print('else')

        await message.copy_to(chat_id=-1001852245312, caption=f"""
Idsi: {message.chat.id}
👤Ismi: {message.from_user.full_name}
ℹ️username: @{message.from_user.username}
🕛vaqt: {datetime.datetime.now()}
✍️Nima dep yozdi yoki nima tashadi: {message.text, message.content_type}
            """
)