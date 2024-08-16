from aiogram.types import Message
from aiogram.filters import Command

from ..routers import user_router as router

@router.message(Command('start'))
async def _start(message: Message):
    await message.answer('Hello, I\'m bot')