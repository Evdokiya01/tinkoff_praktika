import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from config import TOKEN
from user_states import UserStates
from keyboard import keyboards

storage = MemoryStorage()

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=storage)

@dp.message(Command("start"))
async def start(message: types.Message, state: FSMContext):
    kb = keyboards[UserStates.BASE]
    await message.answer("Привет! Я умею следить за Пари", reply_markup=kb)
    await state.set_state(UserStates.BASE)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    print("bot start was completed")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())