import asyncio
import random
from  uuid import uuid4

from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram import F
from aiogram.filters.state import StateFilter

from config import TOKEN
from user_states import UserStates
from keyboard import keyboards
import pari_servise as ps

storage = MemoryStorage()

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=storage)


@dp.message(Command("start"))
async def start(message: types.Message, state: FSMContext):
    kb = keyboards[UserStates.BASE]
    await message.answer("Привет! Я умею следить за Пари", reply_markup=kb)
    await state.set_state(UserStates.BASE)


@dp.message(F.text.lower() == 'создать пари', StateFilter(UserStates.BASE))
async def add_paris(message: types.Message):
    pari_name = str(uuid4())
    ps.add_pari(message.from_user.id, pari_name)
    await message.answer(f'Пари {pari_name} было успешно создано')


@dp.message(F.text.lover() == 'мои пари', StateFilter(UserStates.BASE))
async def get_paris(message: types.Message):
    paris = ps.get_pari(message.from_user.id)
    text = ""
    for pari in paris:
        text += '\n' + pari
    await message.answer(f'Твои пари: {text}')

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    print("bot start was completed")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
