from aiogram import Bot, Dispatcher, executor, types

import matplotlib.pyplot as plt
import os

from token import TOKEN
from classifier import classifyImage


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


plt.show()
@dp.message_handler(content_types=["photo"])
async def test(message):

    await message.photo[-1].download('test.jpg')
    await message.answer(classifyImage("test.jpg"))
    os.remove("test.jpg")


if __name__ == "__main__":
    executor.start_polling(dp)
