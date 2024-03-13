import random
from aiogram import F
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="7083339818:AAF41_9AKe4F3TWCsi1-knMAgkeZvTnkhGg")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Да!")],
        [types.KeyboardButton(text="В следующий раз...")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="Играем?")

    await message.answer("Привет! Это игра угадай число,я загадываю число от 1 до 100, ваша задача отгадать!\n Начнём?", reply_markup=keyboard)

#ДА
@dp.message(F.text.lower() == "да!")
async def yes(message: types.Message):
    await message.reply("Отлично, я загадал число, угадывай!",reply_markup=types.ReplyKeyboardRemove())

#НЕТ
@dp.message(F.text.lower() == "в следующий раз...")
async def no(message: types.Message):
    keb = [
        [types.KeyboardButton(text="/start")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=keb, resize_keyboard=True)
    await message.reply("Ну как знаешь.",reply_markup=keyboard)
#переменная с загаданным числом


@dp.message()
async def user_number(message: types.Message):
    try:
        bot_number = random.randint(1, 100)
        user_number = int(message.text)

        kb = [
            [types.KeyboardButton(text="Да!")],
            [types.KeyboardButton(text="В следующий раз...")]
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="Играем?")

        if user_number == bot_number:
            await message.answer("Поздравляю, ты угадал число!\nСыграем ещё раз?", reply_markup=keyboard)
        elif user_number > 100:
            await message.answer("Введите число от 1 до 100.")
        else:
            await message.answer(f"К сожалению, это не верное число. Я загадал число: {bot_number}\nСыграем ещё раз?", reply_markup=keyboard)
    except ValueError:
        await message.answer("Пожалуйста, введите число от 1 до 100.")



# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())