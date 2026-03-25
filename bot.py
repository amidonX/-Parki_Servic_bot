import os
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

# Бот берет токен из переменной окружения BOT_TOKEN
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(F.text)
async def generate_replies(message: Message):
    # Логика для генерации 3-х ответов для Парков Видное
    replies = (
        "✅ **Вариант 1:** Благодарим за отзыв! Нам очень приятно.\n\n"
        "✅ **Вариант 2:** Спасибо за обратную связь! Ждем вас снова в наших парках.\n\n"
        "✅ **Вариант 3:** Рады, что вам понравилось! С уважением, команда МБУ «Парки Видное»."
    )
    await message.answer(replies)

async def main():
    print("Бот запущен и готов помогать!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
