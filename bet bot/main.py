from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from time import sleep
from data_base import add_filt_three
from filt_two import supec
from parce import filt_one_two, three_control
from data_base import get_three, grom, get_block_list


bot = Bot("6212269832:AAHONSk4HhjKxMRRPAyPW3e-gOlhSa1lTpQ")  # Токен бота

dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def main(message: types.Message):
    inline_kb = InlineKeyboardMarkup()
    grom_button = InlineKeyboardButton("Заблокировать лигу", callback_data="grom")
    inline_kb.add(grom_button)

    await bot.send_message(message.from_user.id, "Я запущен!")
    filt = [] #Список для матчей за которыми ведется контроль
    while True:
        los = filt_one_two() #Получаем список матчей(ссылки)  
        for num in los: #Для кажого матча из los
            if num in filt: # Смортим, ведётся ли уже контроль за данным матчем 
                pass # Если да, то пропускаем его 
            else: # Иначе отправляем в бота сигнал о подходящем матче
                global gh
                gh = supec(num) # Получаем инфу о матче для отправки 
                print(f"\nЛига: {gh[0]}\n\n{gh[1]} vs {gh[2]}\n\nСчёт: {gh[3]}:{gh[4]}\n")
                sleep(1)
                send_three = await bot.send_message(message.from_user.id, f"\n⚽️ Лига: {gh[0]} ⚽️\n\n🔰 {gh[1]} vs {gh[2]} 🔰\n\n⚜️ Счёт: {gh[3]}:{gh[4]} ⚜️\n", reply_markup=inline_kb) # Шлём инфуо подошедшем матче в бота
                add_filt_three(send_three["message_id"], num, gh[3], gh[4]) #Добаляем в базу данных инфу о матче за которым продолжим наблюдать
                filt.append(num) #Добавляем матч в список для контроля уже просигнализированных матчей

        tuy = get_three() #Получаем инфу о матчах в БД (Тех за которыми наблюдаем)
        for lam in tuy: #Для каждого из этих матчей
            try: #Чекаем счёт, если функция вернула значение, меняем сообщение
                uni = three_control(lam) #Чекаем счёт
                print(uni)
                await bot.edit_message_text(text=f"\n⚽️ Лига: {gh[0]} ⚽️\n\n🔰 {gh[1]} vs {gh[2]} 🔰\n\n⚜️ Счёт: {uni[1]}:{uni[2]} ⚜️\n\n✅ Goals: {uni[3]} ✅", message_id=uni[0]) #Изменяем сообщение
            except:
                continue #Инчае продолжаем чекать все матчи в БД

@dp.callback_query_handler(lambda c: c.data == "grom")
async def process_callback_grom(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await grom(gh[0])

@dp.message_handler(commands='block')
async def main(message: types.Message):
    await bot.send_message(message.from_user.id, get_block_list())
    await bot.send_message(message.from_user.id, "Для того что бы удалить Лигу из Чёрного списка отправь мне её название")



if __name__ == "__main__":
	executor.start_polling(dp)

