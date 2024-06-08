

from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo


bot = Bot(token="7199786672:AAGRL5QW97-lYeYWCToQPQV3IM_KsWpGcxc")
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(f"Hello {message.from_user.full_name}!")
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="Subscribe", url="https://t.me/stendoff_2_chaths"))
    keyboard.add(InlineKeyboardButton(text="Subscribed✅", callback_data="subscribed"))
    await message.answer("Subscribe to channels to use bot!", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data == 'subscribed')
async def callback_subscribe(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(image="Eco-Coin-800x600-1.jpeg", text="Click to Explore", web_app=WebAppInfo(
        url='https://otabeknormuminov.github.io/Ecocoin.world/')))
    await call.message.answer(
        "Supporting the planet is at the core of ECocoin's mission. Every transaction and action taken with ECocoin contributes to a healthier environment. Users are rewarded for making eco-friendly choices and supporting sustainability initiatives. Being part of the ECocoin community means joining a global movement dedicated to making a positive impact on the planet. The innovative technology behind ECocoin provides security, transparency, and efficiency tailored for sustainability.",
        reply_markup=markup
    )



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

