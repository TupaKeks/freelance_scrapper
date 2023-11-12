import asyncio
import time

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from main import get_content
from aiogram.utils.keyboard import InlineKeyboardBuilder

token = "6530594275:AAGImmRV7tkK5LwXYXIp7S3Me7epTlab2kM"

bot = Bot(token)
dp = Dispatcher()

content = get_content()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.reply("Hello!")


@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.reply("Type something and I'll respond!\n"
                        "Also you can type /buttons and I will show you some special buttons to use :)")


@dp.message(Command("buttons"))
async def cmd_button(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="Запросить геолокацию", request_location=True),
        types.KeyboardButton(text="Запросить контакт", request_contact=True)
    )
    builder.row(types.KeyboardButton(
        text="Создать викторину:",
        request_poll=types.KeyboardButtonPollType(type="quiz")
    ))
    await message.answer(
        "Выберите действие:",
        reply_markup=builder.as_markup(resize_keyboard=True),
    )


@dp.message(Command('parser'))
async def cmd_parser(message: types.Message):
    try:
        # Iterate over the key-value pairs of the dictionary
        for key, value in content.items():
            # Send each key-value pair as a separate message
            await message.reply(f'{key}: {value}')
        print(content)

    except Exception as e:
        print(f"An error occurred: {e}")
        await message.reply("An error occurred while processing the command.")


@dp.message()
async def cmd_message(message: types.Message):
    await message.answer(message.text)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
