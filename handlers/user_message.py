from aiogram import F, Router, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message

from filters import AdminProtect
import keyboards as kb
from database import insert_user

user = Router()

@user.message(CommandStart())
async def start_command(message: Message):
    admin = AdminProtect()
    if not await admin(message):  # Добавляем await здесь
        await message.answer(f"Привет, {message.from_user.full_name}!\n")
        await insert_user(message.from_user.id, message.from_user.username)
    else:
        await message.answer(f"Привет, {message.from_user.full_name}!\n")
        await insert_user(message.from_user.id, message.from_user.username)
        await message.answer(f"Вы успешно авторизовались как администратор!",
                             reply_markup=kb.admin_menu)
