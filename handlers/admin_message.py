from aiogram import F, Router, Bot
from aiogram.types import Message

from filters import AdminProtect
import keyboards as kb


admin = Router()

@admin.message(AdminProtect(), F.text == "Админ-панель")
async def admin_panel(message: Message):
    await message.answer(f"Вы вошли в админ-панель!\n"
                         f"Выберите действие",
                         reply_markup=kb.admin_panel)