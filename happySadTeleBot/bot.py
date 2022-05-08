from ast import arguments
from aiogram import Bot, Dispatcher, executor, types
from classifier import classifyImage
import matplotlib.pyplot as plt
import os

bot = Bot(token="5346782906:AAGuSoPx1rBt1xDSjI7LQVeVDvzo0ewWY84")
dp = Dispatcher(bot)


plt.show()
@dp.message_handler(content_types=["photo"])
async def test(message):

    await message.photo[-1].download('test.jpg')
    await message.answer(classifyImage("test.jpg"))
    os.remove("test.jpg")


if __name__ == "__main__":
    executor.start_polling(dp)
