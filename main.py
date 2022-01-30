api_token='Bot Token'
salomlashish=['salom','assalomu alaykum','assalomu alaeykum','salomalikum']
xayrlashish=['xayr',"sog' bo'ling"]
from aiogram import Bot,Dispatcher,executor,types

bot=Bot(token=api_token)
dp=Dispatcher(bot)
@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f"Salom foydalanuvchi")
@dp.message_handler(content_types='text')
async def test(message:types.Message):
    text=message.text
    text=text.lower()
    if text in salomlashish:
        await message.answer("Salom berdiz Salomat bo'ling")
    if text in xayrlashish:
        await message.answer("Xayrlashdiz, Omad.")
    if text not in xayrlashish and text not in salomlashish:
        await  message.answer("Tushunmadim gapingizga?!")
if __name__=="__main__":
    executor.start_polling(dp)
