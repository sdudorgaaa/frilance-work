from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import sqlite3


TOKEN = '5738161405:AAGrLEPSLoxlVX42kftCfS3h3ioaHj7Jow4'


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


db = sqlite3.connect('bang.db')
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id INT,
    user_name TEXT
)""")
db.commit()


avaliable_school_class = ["1кл","2кл","3кл","4кл","5кл","6кл","7кл","8кл","9кл","10кл","11кл","Факультативы"]
aviable_school_day = ["Пн","Вт","Ср","Чт","Пт","Сб","Расписание звонков","Назад","Замены","Помощь"]
avaliable_facts_day = ["Пн","Вт","Ср","Чт","Пт","Сб","Назад"]


class Schedule(StatesGroup):
    choosing_school_class = State()
    choosing_school_day = State()
    finish = State()

class Admin(StatesGroup):
    text = State()

class Facts(StatesGroup):
    choosing_facts_day = State()

class Schedule_two(StatesGroup):
    choosing_school_class_two = State()


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message, state: FSMContext):
    kb = [
        [types.KeyboardButton(text="1кл"),
        types.KeyboardButton(text="2кл"),
        types.KeyboardButton(text="3кл")],
        [types.KeyboardButton(text="4кл"),
        types.KeyboardButton(text="5кл"),
        types.KeyboardButton(text="6кл")],
        [types.KeyboardButton(text="7кл"),
        types.KeyboardButton(text="8кл"),
        types.KeyboardButton(text="9кл")],
        [types.KeyboardButton(text="10кл"),
        types.KeyboardButton(text="Факультативы"),
        types.KeyboardButton(text="11кл")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="Выберите класс")

    sql.execute(f"SELECT user_id FROM users WHERE user_id = '{message.from_user.id}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (?, ?)", (message.from_user.id, message.from_user.first_name))
        db.commit()

    await bot.send_message(message.from_user.id, f"Привет {message.from_user.first_name}!\
        \n\nЭто бот, который поможет тебе удобно и быстро узнавать расписание!\
        \n\nПросто выбери нужный класс", reply_markup=keyboard)
    await Schedule.choosing_school_class.set()

@dp.message_handler(
    state = Schedule.choosing_school_class,
    text=avaliable_school_class
) 
async def school_class(message: types.Message, state: FSMContext): 
    await state.update_data(chosen_school_class = message.text)
    user_data = await state.get_data()
    school_class = user_data['chosen_school_class']
    if school_class == "Факультативы":
        kb1 = [
            [types.KeyboardButton(text="Пн"),
            types.KeyboardButton(text="Вт"),
            types.KeyboardButton(text="Ср")],
            [types.KeyboardButton(text="Чт"),
            types.KeyboardButton(text="Пт"),
            types.KeyboardButton(text="Сб")],
            [types.KeyboardButton(text="Назад")]
        ]
        keyboard1 = types.ReplyKeyboardMarkup(keyboard=kb1, resize_keyboard=True, input_field_placeholder="Выберите день недели")
        await bot.send_message (message.from_user.id, "Выбери день недели", reply_markup=keyboard1)
        await state.finish()
        await Facts.choosing_facts_day.set()

        @dp.message_handler(
        state=Facts.choosing_facts_day,
        text = avaliable_facts_day
        )   
        async def fin_facts(message: types.Message, state: FSMContext):
            await state.update_data(chosen_facts_day = message.text)
            user_data = await state.get_data()
            facts_day = user_data['chosen_facts_day']
            match facts_day:
                case 'Пн':
                    from facts import monday_prepod, monday_facult_name, monday_school_class, monday_time, monday_kab
                    await bot.send_message (message.from_user.id, f"Учитель: {monday_prepod()}\nЗанятие: {monday_facult_name()}\nКласс: {monday_school_class()}\nВремя: {monday_time()}\nКабинет: {monday_kab()}", reply_markup=keyboard1)

                case'Вт':
                    from facts import tuesday_facult_name_one, tuesday_facult_name_three, tuesday_facult_name_two, tuesday_kab_one, tuesday_kab_three, tuesday_kab_two,\
                        tuesday_prepod_one, tuesday_prepod_three, tuesday_prepod_two, tuesday_school_class_one,\
                        tuesday_school_class_three, tuesday_school_class_two, tuesday_time_one, tuesday_time_three, tuesday_time_two
                    await bot.send_message (message.from_user.id, f"Учитель: {tuesday_prepod_one()}\nЗанятие: {tuesday_facult_name_one()}\nКласс: {tuesday_school_class_one()}\nВремя: {tuesday_time_one()}\nКабинет: {tuesday_kab_one()}", reply_markup=keyboard1)
                    await bot.send_message (message.from_user.id, f"Учитель: {tuesday_prepod_two()}\nЗанятие: {tuesday_facult_name_two()}\nКласс: {tuesday_school_class_two()}\nВремя: {tuesday_time_two()}\nКабинет: {tuesday_kab_two()}", reply_markup=keyboard1)
                    await bot.send_message (message.from_user.id, f"Учитель: {tuesday_prepod_three()}\nЗанятие: {tuesday_facult_name_three()}\nКласс: {tuesday_school_class_three()}\nВремя: {tuesday_time_three()}\nКабинет: {tuesday_kab_three()}", reply_markup=keyboard1)

                case'Ср':
                    from facts import wensday_facult_name_one, wensday_facult_name_two, wensday_kab_one, wensday_kab_two, wensday_prepod_one,\
                        wensday_prepod_two, wensday_school_class_one, wensday_school_class_two, wensday_time_one, wensday_time_two
                    await bot.send_message (message.from_user.id, f"Учитель: {wensday_prepod_one()}\nЗанятие: {wensday_facult_name_one()}\nКласс: {wensday_school_class_one()}\nВремя: {wensday_time_one()}\nКабинет: {wensday_kab_one()}", reply_markup=keyboard1)
                    await bot.send_message (message.from_user.id, f"Учитель: {wensday_prepod_two()}\nЗанятие: {wensday_facult_name_two()}\nКласс: {wensday_school_class_two()}\nВремя: {wensday_time_two()}\nКабинет: {wensday_kab_two()}", reply_markup=keyboard1)

                case'Чт':
                    await bot.send_message (message.from_user.id, "Факультативов нету", reply_markup=keyboard1)

                case'Пт':
                    from facts import friday_facult_name_four, friday_facult_name_one, friday_facult_name_three, friday_facult_name_two, friday_kab_four, friday_kab_one, friday_kab_three, friday_kab_two, friday_prepod_four, friday_prepod_one, friday_prepod_three,\
                        friday_prepod_two, friday_school_class_four, friday_school_class_one, friday_school_class_three, friday_school_class_two, friday_time_four, friday_time_one, friday_time_three, friday_time_two
                    await bot.send_message (message.from_user.id, f"Учитель: {friday_prepod_one()}\nЗанятие: {friday_facult_name_one()}\nКласс: {friday_school_class_one()}\nВремя: {friday_time_one()}\nКабинет: {friday_kab_one()}", reply_markup=keyboard1)
                    await bot.send_message (message.from_user.id, f"Учитель: {friday_prepod_two()}\nЗанятие: {friday_facult_name_two()}\nКласс: {friday_school_class_two()}\nВремя: {friday_time_two()}\nКабинет: {friday_kab_two()}", reply_markup=keyboard1)
                    await bot.send_message (message.from_user.id, f"Учитель: {friday_prepod_three()}\nЗанятие: {friday_facult_name_three()}\nКласс: {friday_school_class_three()}\nВремя: {friday_time_three()}\nКабинет: {friday_kab_three()}", reply_markup=keyboard1)
                    await bot.send_message (message.from_user.id, f"Учитель: {friday_prepod_four()}\nЗанятие: {friday_facult_name_four()}\nКласс: {friday_school_class_four()}\nВремя: {friday_time_four()}\nКабинет: {friday_kab_four()}", reply_markup=keyboard1)

                case'Сб':
                    from facts import saturday_facult_name_five, saturday_facult_name_four, saturday_facult_name_one, saturday_facult_name_three, saturday_facult_name_two, saturday_kab_five, saturday_kab_four, saturday_kab_one, saturday_kab_three, saturday_kab_two,\
                        saturday_prepod_five, saturday_prepod_four, saturday_prepod_one, saturday_prepod_three, saturday_prepod_two, saturday_school_class_five, saturday_school_class_four, saturday_school_class_one, saturday_school_class_three, saturday_school_class_two,\
                            saturday_time_five, saturday_time_four, saturday_time_one, saturday_time_three, saturday_time_two
                    await bot.send_message (message.from_user.id, f"Учитель: {saturday_prepod_one()}\nЗанятие: {saturday_facult_name_one()}\nКласс: {saturday_school_class_one()}\nВремя: {saturday_time_one()}\nКабинет: {saturday_kab_one()}", reply_markup=keyboard1)
                    await bot.send_message (message.from_user.id, f"Учитель: {saturday_prepod_two()}\nЗанятие: {saturday_facult_name_two()}\nКласс: {saturday_school_class_two()}\nВремя: {saturday_time_two()}\nКабинет: {saturday_kab_two()}", reply_markup=keyboard1)
                    await bot.send_message (message.from_user.id, f"Учитель: {saturday_prepod_three()}\nЗанятие: {saturday_facult_name_three()}\nКласс: {saturday_school_class_three()}\nВремя: {saturday_time_three()}\nКабинет: {saturday_kab_three()}", reply_markup=keyboard1)
                    await bot.send_message (message.from_user.id, f"Учитель: {saturday_prepod_four()}\nЗанятие: {saturday_facult_name_four()}\nКласс: {saturday_school_class_four()}\nВремя: {saturday_time_four()}\nКабинет: {saturday_kab_four()}", reply_markup=keyboard1)
                    await bot.send_message (message.from_user.id, f"Учитель: {saturday_prepod_five()}\nЗанятие: {saturday_facult_name_five()}\nКласс: {saturday_school_class_five()}\nВремя: {saturday_time_five()}\nКабинет: {saturday_kab_five()}", reply_markup=keyboard1)

                case 'Назад':
                    await state.finish()
                    kb = [
                    [types.KeyboardButton(text="1кл"),
                    types.KeyboardButton(text="2кл"),
                    types.KeyboardButton(text="3кл")],
                    [types.KeyboardButton(text="4кл"),
                    types.KeyboardButton(text="5кл"),
                    types.KeyboardButton(text="6кл")],
                    [types.KeyboardButton(text="7кл"),
                    types.KeyboardButton(text="8кл"),
                    types.KeyboardButton(text="9кл")],
                    [types.KeyboardButton(text="10кл"),
                    types.KeyboardButton(text="Факультативы"),
                    types.KeyboardButton(text="11кл")]
                    ]
                    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="Выберите класс")
                    await bot.send_message (message.from_user.id, "Вы вернулись назад", reply_markup=keyboard)
                    await Schedule.choosing_school_class.set()

    else:
        kb1 = [
            [types.KeyboardButton(text="Пн"),
            types.KeyboardButton(text="Вт"),
            types.KeyboardButton(text="Ср")],
            [types.KeyboardButton(text="Чт"),
            types.KeyboardButton(text="Пт"),
            types.KeyboardButton(text="Сб")],
            [types.KeyboardButton(text="Замены")]
        ]
        keyboard1 = types.ReplyKeyboardMarkup(keyboard=kb1, resize_keyboard=True, input_field_placeholder="Выберите день недели")
        await bot.send_message (message.from_user.id, "Теперь выбери день недели", reply_markup=keyboard1)
        await Schedule.next()

@dp.message_handler(
    state=Schedule.choosing_school_day,
    text = aviable_school_day
)   
async def finish(message: types.Message, state: FSMContext):
    kb11 = [
        [types.KeyboardButton(text="Пн"),
        types.KeyboardButton(text="Вт"),
        types.KeyboardButton(text="Ср")],
        [types.KeyboardButton(text="Чт"),
        types.KeyboardButton(text="Пт"),
        types.KeyboardButton(text="Сб")],
        [types.KeyboardButton(text="Расписание звонков"),
        types.KeyboardButton(text="Замены")],
        [types.KeyboardButton(text="Назад"),
         types.KeyboardButton(text="Помощь")]
        ]
    keyboard11 = types.ReplyKeyboardMarkup(keyboard=kb11, resize_keyboard=True)
    await state.update_data(chosen_school_day = message.text)
    user_data = await state.get_data()
    school_class = user_data['chosen_school_class']
    school_day = user_data['chosen_school_day']
    match school_day:
        case 'Пн':
            match school_class:
                case "1кл":
                    from schedule_xlrd import monday_one_one, monday_one_two, monday_one_three, monday_one_four
                    await bot.send_message(message.from_user.id, f"1.{monday_one_one()}\n2.{monday_one_two()}\n3.{monday_one_three()}\n4.{monday_one_four()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()
                    
                case "2кл":
                    from schedule_xlrd import monday_two_one, monday_two_two, monday_two_three, monday_two_four
                    await bot.send_message(message.from_user.id, f"1.{monday_two_one()}\n2.{monday_two_two()}\n3.{monday_two_three()}\n4.{monday_two_four()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case "3кл":
                    from schedule_xlrd import monday_three_one, monday_three_two, monday_three_three, monday_three_four, monday_three_five
                    await bot.send_message(message.from_user.id, f"1.{monday_three_one()}\n2.{monday_three_two()}\n3.{monday_three_three()}\n4.{monday_three_four()}\n5.{monday_three_five()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case "4кл":
                    from schedule_xlrd import monday_four_one, monday_four_two, monday_four_three, monday_four_four
                    await bot.send_message(message.from_user.id, f"1.{monday_four_one()}\n2.{monday_four_two()}\n3.{monday_four_three()}\n4.{monday_four_four()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case "5кл":
                    from schedule_xlrd import monday_five_one, monday_five_two, monday_five_three, monday_five_four, monday_five_five, monday_five_six
                    await bot.send_message(message.from_user.id, f"1.{monday_five_one()}\n2.{monday_five_two()}\n3.{monday_five_three()}\n4.{monday_five_four()}\n5.{monday_five_five()}\n6.{monday_five_six()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case "6кл":
                    from schedule_xlrd import monday_six_one, monday_six_two, monday_six_three, monday_six_four, monday_six_five, monday_six_six
                    await bot.send_message(message.from_user.id, f"1.{monday_six_one()}\n2.{monday_six_two()}\n3.{monday_six_three()}\n4.{monday_six_four()}\n5.{monday_six_five()}\n6.{monday_six_six()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case "7кл":
                    from schedule_xlrd import monday_seven_one, monday_seven_two, monday_seven_three, monday_seven_four, monday_seven_five, monday_seven_six
                    await bot.send_message(message.from_user.id, f"1.{monday_seven_one()}\n2.{monday_seven_two()}\n3.{monday_seven_three()}\n4.{monday_seven_four()}\n5.{monday_seven_five()}\n6.{monday_seven_six()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case "8кл":
                    from schedule_xlrd import monday_eight_one, monday_eight_two, monday_eight_three, monday_eight_four, monday_eight_five, monday_eight_six, monday_eight_seven
                    await bot.send_message(message.from_user.id, f"1.{monday_eight_one()}\n2.{monday_eight_two()}\n3.{monday_eight_three()}\n4.{monday_eight_four()}\n5.{monday_eight_five()}\n6.{monday_eight_six()}\n7.{monday_eight_seven()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case "9кл":
                    from schedule_xlrd import monday_nine_one, monday_nine_two, monday_nine_three, monday_nine_four, monday_nine_five, monday_nine_six
                    await bot.send_message(message.from_user.id, f"1.{monday_nine_one()}\n2.{monday_nine_two()}\n3.{monday_nine_three()}\n4.{monday_nine_four()}\n5.{monday_nine_five()}\n6.{monday_nine_six()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case "10кл":
                    from schedule_xlrd import monday_ten_one, monday_ten_two, monday_ten_three, monday_ten_four, monday_ten_five, monday_ten_six
                    await bot.send_message(message.from_user.id, f"1.{monday_ten_one()}\n2.{monday_ten_two()}\n3.{monday_ten_three()}\n4.{monday_ten_four()}\n5.{monday_ten_five()}\n6.{monday_ten_six()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case "11кл":
                    from schedule_xlrd import monday_eleven_one, monday_eleven_two, monday_eleven_three, monday_eleven_four, monday_eleven_five, monday_eleven_six
                    await bot.send_message(message.from_user.id, f"1.{monday_eleven_one()}\n2.{monday_eleven_two()}\n3.{monday_eleven_three()}\n4.{monday_eleven_four()}\n5.{monday_eleven_five()}\n6.{monday_eleven_six()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()
                                              
        case 'Вт':
            match school_class:
                case "1кл":
                    from schedule_xlrd import tuesday_one_one, tuesday_one_two, tuesday_one_three, tuesday_one_four
                    await bot.send_message(message.from_user.id, f"1.{tuesday_one_one()}\n2.{tuesday_one_two()}\n3.{tuesday_one_three()}\n4.{tuesday_one_four()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case "2кл":
                    from schedule_xlrd import tuesday_two_one, tuesday_two_two, tuesday_two_three, tuesday_two_four
                    await bot.send_message(message.from_user.id, f"1.{tuesday_two_one()}\n2.{tuesday_two_two()}\n3.{tuesday_two_three()}\n4.{tuesday_two_four()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case "3кл":
                    from  schedule_xlrd import tuesday_three_one, tuesday_three_two, tuesday_three_three, tuesday_three_four, tuesday_three_five
                    await bot.send_message(message.from_user.id, f"1.{tuesday_three_one()}\n2.{tuesday_three_two()}\n3.{tuesday_three_three()}\n4.{tuesday_three_four()}\n5.{tuesday_three_five()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case "4кл":
                    from schedule_xlrd import tuesday_four_one, tuesday_four_two, tuesday_four_three, tuesday_four_four, tuesday_four_five
                    await bot.send_message(message.from_user.id, f"1.{tuesday_four_one()}\n2.{tuesday_four_two()}\n3.{tuesday_four_three()}\n4.{tuesday_four_four()}\n5.{tuesday_four_five()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case "5кл":
                    from schedule_xlrd import tuesday_five_one, tuesday_five_two, tuesday_five_three, tuesday_five_four, tuesday_five_five, tuesday_five_six
                    await bot.send_message(message.from_user.id, f"1.{tuesday_five_one()}\n2.{tuesday_five_two()}\n3.{tuesday_five_three()}\n4.{tuesday_five_four()}\n5.{tuesday_five_five()}\n6.{tuesday_five_six()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case "6кл":
                    from schedule_xlrd import tuesday_six_one, tuesday_six_two, tuesday_six_three, tuesday_six_four, tuesday_six_five, tuesday_six_six
                    await bot.send_message(message.from_user.id, f"1.{tuesday_six_one()}\n2.{tuesday_six_two()}\n3.{tuesday_six_three()}\n4.{tuesday_six_four()}\n5.{tuesday_six_five()}\n6.{tuesday_six_six()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case "7кл":
                    from schedule_xlrd import tuesday_seven_one, tuesday_seven_two, tuesday_seven_three, tuesday_seven_four, tuesday_seven_five, tuesday_seven_six
                    await bot.send_message(message.from_user.id, f"1.{tuesday_seven_one()}\n2.{tuesday_seven_two()}\n3.{tuesday_seven_three()}\n4.{tuesday_seven_four()}\n5.{tuesday_seven_five()}\n6.{tuesday_seven_six()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case "8кл":
                    from schedule_xlrd import tuesday_eight_one, tuesday_eight_two, tuesday_eight_three, tuesday_eight_four, tuesday_eight_five, tuesday_eight_six
                    await bot.send_message(message.from_user.id, f"1.{tuesday_eight_one()}\n2.{tuesday_eight_two()}\n3.{tuesday_eight_three()}\n4.{tuesday_eight_four()}\n5.{tuesday_eight_five()}\n6.{tuesday_eight_six()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case "9кл":
                    from schedule_xlrd import tuesday_nine_one, tuesday_nine_two, tuesday_nine_three, tuesday_nine_four, tuesday_nine_five, tuesday_nine_six, tuesday_nine_seven
                    await bot.send_message(message.from_user.id, f"1.{tuesday_nine_one()}\n2.{tuesday_nine_two()}\n3.{tuesday_nine_three()}\n4.{tuesday_nine_four()}\n5.{tuesday_nine_five()}\n6.{tuesday_nine_six()}\n7.{tuesday_nine_seven()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case "10кл":
                    from schedule_xlrd import tuesday_ten_one, tuesday_ten_two, tuesday_ten_three, tuesday_ten_four, tuesday_ten_five, tuesday_ten_six
                    await bot.send_message(message.from_user.id, f"1.{tuesday_ten_one()}\n2.{tuesday_ten_two()}\n3.{tuesday_ten_three()}\n4.{tuesday_ten_four()}\n5.{tuesday_ten_five()}\n6.{tuesday_ten_six()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case "11кл":
                    from schedule_xlrd import tuesday_eleven_one, tuesday_eleven_two, tuesday_eleven_three, tuesday_eleven_four, tuesday_eleven_five, tuesday_eleven_six
                    await bot.send_message(message.from_user.id, f"1.{tuesday_eleven_one()}\n2.{tuesday_eleven_two()}\n3.{tuesday_eleven_three()}\n4.{tuesday_eleven_four()}\n5.{tuesday_eleven_six()}\n6.{tuesday_eleven_two()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

        case 'Ср':
            match school_class:
                case '1кл':
                    from schedule_xlrd import wensday_one_one, wensday_one_two, wensday_one_three, wensday_one_four
                    await bot.send_message(message.from_user.id, f"1.{wensday_one_one()}\n2.{wensday_one_two()}\n3.{wensday_one_three()}\n4.{wensday_one_four()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '2кл':
                    from schedule_xlrd import wensday_two_one, wensday_two_two, wensday_two_three, wensday_two_four, wensday_two_five
                    await bot.send_message(message.from_user.id, f"1.{wensday_two_one()}\n2.{wensday_two_two()}\n3.{wensday_two_three()}\n4.{wensday_two_four()}\n5.{wensday_two_five()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '3кл':
                    from schedule_xlrd import wensday_three_one, wensday_three_two, wensday_three_three, wensday_three_four, wensday_three_five
                    await bot.send_message(message.from_user.id, f"1.{wensday_three_one()}\n2.{wensday_three_two()}\n3.{wensday_three_three()}\n4.{wensday_three_four()}\n5.{wensday_three_five()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '4кл':
                    from schedule_xlrd import wensday_four_one, wensday_four_two, wensday_four_three, wensday_four_four, wensday_four_five
                    await bot.send_message(message.from_user.id, f"1.{wensday_four_one()}\n2.{wensday_four_two()}\n3.{wensday_four_three()}\n4.{wensday_four_four()}\n5.{wensday_four_five()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '5кл':
                    from schedule_xlrd import wensday_five_one, wensday_five_two, wensday_five_three, wensday_five_four, wensday_five_five
                    await bot.send_message(message.from_user.id, f"1.{wensday_five_one()}\n2.{wensday_five_two()}\n3.{wensday_five_three()}\n4.{wensday_five_four()}\n5.{wensday_five_five()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '6кл':
                    from schedule_xlrd import wensday_six_one, wensday_six_two, wensday_six_three, wensday_six_four, wensday_six_five, wensday_six_six
                    await bot.send_message(message.from_user.id, f"1.{wensday_six_one()}\n2.{wensday_six_two()}\n3.{wensday_six_three()}\n4.{wensday_six_four()}\n5.{wensday_six_five()}\n6.{wensday_six_six()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '7кл':
                    from schedule_xlrd import wensday_seven_one, wensday_seven_two, wensday_seven_three, wensday_seven_four, wensday_seven_five, wensday_seven_six, wensday_seven_seven
                    await bot.send_message(message.from_user.id, f"1.{wensday_seven_one()}\n2.{wensday_seven_two()}\n3.{wensday_seven_three()}\n4.{wensday_seven_four()}\n5.{wensday_seven_five()}\n6.{wensday_seven_six()}\n7.{wensday_seven_seven()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '8кл':
                    from schedule_xlrd import wensday_eight_one, wensday_eight_two, wensday_eight_three, wensday_eight_four, wensday_eight_five, wensday_eight_six, wensday_eight_seven
                    await bot.send_message(message.from_user.id, f"1.{wensday_eight_one()}\n2.{wensday_eight_two()}\n3.{wensday_eight_three()}\n4.{wensday_eight_four()}\n5.{wensday_eight_five()}\n6.{wensday_eight_six()}\n7.{wensday_eight_seven()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()
                
                case '9кл':
                    from schedule_xlrd import wensday_nine_one, wensday_nine_two, wensday_nine_three, wensday_nine_four, wensday_nine_five, wensday_nine_six
                    await bot.send_message(message.from_user.id, f"1.{wensday_nine_one()}\n2.{wensday_nine_two()}\n3.{wensday_nine_three()}\n4.{wensday_nine_four()}\n5.{wensday_nine_five()}\n6.{wensday_nine_six()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '10кл':
                    from schedule_xlrd import wensday_ten_one, wensday_ten_two, wensday_ten_three, wensday_ten_four, wensday_ten_five, wensday_ten_six, wensday_ten_seven
                    await bot.send_message(message.from_user.id, f"1.{wensday_ten_one()}\n2.{wensday_ten_two()}\n3.{wensday_ten_three()}\n4.{wensday_ten_four()}\n5.{wensday_ten_five()}\n6.{wensday_ten_six()}\n7.{wensday_ten_seven()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '11кл':
                    from schedule_xlrd import wensday_eleven_one, wensday_eleven_two, wensday_eleven_three, wensday_eleven_four, wensday_eleven_five, wensday_eleven_six, wensday_eleven_seven
                    await bot.send_message(message.from_user.id, f"1.{wensday_eleven_one()}\n2.{wensday_eleven_two()}\n3.{wensday_eleven_three()}\n4.{wensday_eleven_four()}\n5.{wensday_eleven_five()}\n6.{wensday_eleven_six()}\n7.{wensday_eleven_seven()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

        case 'Чт':
            match school_class:
                case '1кл':
                    from schedule_xlrd import thursday_one_one, thursday_one_two, thursday_one_three
                    await bot.send_message(message.from_user.id, f"1.{thursday_one_one()}\n2.{thursday_one_two()}\n3.{thursday_one_three()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '2кл':
                    from schedule_xlrd import thursday_two_one, thursday_two_two, thursday_two_three, thursday_two_four
                    await bot.send_message(message.from_user.id, f"1.{thursday_two_one()}\n2.{thursday_two_two()}\n3.{thursday_two_three()}\n4.{thursday_two_four()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '3кл':
                    from schedule_xlrd import thursday_three_one, thursday_three_two, thursday_three_three, thursday_three_four, thursday_three_five
                    await bot.send_message(message.from_user.id, f"1.{thursday_three_one()}\n2.{thursday_three_two()}\n3.{thursday_three_three()}\n4.{thursday_three_four()}\n5.{thursday_three_five()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '4кл':
                    from schedule_xlrd import thursday_four_one, thursday_four_two, thursday_four_three, thursday_four_four,thursday_four_five
                    await bot.send_message(message.from_user.id, f"1.{thursday_four_one()}\n2.{thursday_four_two()}\n3.{thursday_four_three()}\n4.{thursday_four_four()}\n5.{thursday_four_five()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '5кл':
                    from schedule_xlrd import thursday_five_one, thursday_five_two, thursday_five_three, thursday_five_four, thursday_five_five
                    await bot.send_message(message.from_user.id, f"1.{thursday_five_one()}\n2.{thursday_five_two()}\n3.{thursday_five_three()}\n4.{thursday_five_four()}\n5.{thursday_five_five()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '6кл':
                    from schedule_xlrd import thursday_six_one, thursday_six_two, thursday_six_three, thursday_six_four, thursday_six_five
                    await bot.send_message(message.from_user.id, f"1.{thursday_six_one()}\n2.{thursday_six_two()}\n3.{thursday_six_three()}\n4.{thursday_six_four()}\n5.{thursday_six_five()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '7кл':
                    from schedule_xlrd import thursday_seven_one, thursday_seven_two, thursday_seven_three, thursday_seven_four, thursday_seven_five, thursday_seven_six
                    await bot.send_message(message.from_user.id, f"1.{thursday_seven_one()}\n2.{thursday_seven_two()}\n3.{thursday_seven_three()}\n4.{thursday_seven_four()}\n5.{thursday_seven_five()}\n6.{thursday_seven_six()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '8кл':
                    from schedule_xlrd import thursday_eight_one, thursday_eight_two, thursday_eight_three, thursday_eight_four, thursday_eight_five, thursday_eight_six
                    await bot.send_message(message.from_user.id, f"1.{thursday_eight_one()}\n2.{thursday_eight_two()}\n3.{thursday_eight_three()}\n4.{thursday_eight_four()}\n5.{thursday_eight_five()}\n6.{thursday_eight_six()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()
                
                case '9кл':
                    from schedule_xlrd import thursday_nine_one, thursday_nine_two, thursday_nine_three, thursday_nine_four, thursday_nine_five, thursday_nine_six
                    await bot.send_message(message.from_user.id, f"1.{thursday_nine_one()}\n2.{thursday_nine_two()}\n3.{thursday_nine_three()}\n4.{thursday_nine_four()}\n5.{thursday_nine_five()}\n6.{thursday_nine_six()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '10кл':
                    from schedule_xlrd import thursday_ten_one, thursday_ten_two, thursday_ten_three, thursday_ten_four, thursday_ten_five, thursday_ten_six
                    await bot.send_message(message.from_user.id, f"1.{thursday_ten_one()}\n2.{thursday_ten_two()}\n3.{thursday_ten_three()}\n4.{thursday_ten_four()}\n5.{thursday_ten_five()}\n6.{thursday_ten_six()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '11кл':
                    from schedule_xlrd import thursday_eleven_one, thursday_eleven_two, thursday_eleven_three, thursday_eleven_four, thursday_eleven_five, thursday_eleven_six, thursday_eleven_seven
                    await bot.send_message(message.from_user.id, f"1.{thursday_eleven_one()}\n2.{thursday_eleven_two()}\n3.{thursday_eleven_three()}\n4.{thursday_eleven_four()}\n5.{thursday_eleven_five()}\n6.{thursday_eleven_six()}\n7.{thursday_eleven_seven()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()
            
        case 'Пт':
            match school_class:
                case '1кл':
                    from schedule_xlrd import friday_one_one, friday_one_two, friday_one_three, monday_one_four
                    await bot.send_message(message.from_user.id, f"1.{friday_one_one()}\n2.{friday_one_two()}\n3.{friday_one_three()}\n4.{monday_one_four()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '2кл':
                    from schedule_xlrd import friday_two_one, friday_two_two, friday_two_three, friday_two_four
                    await bot.send_message(message.from_user.id, f"1.{friday_two_one()}\n2.{friday_two_two()}\n3.{friday_two_three()}\n4.{friday_two_four()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '3кл':
                    from schedule_xlrd import friday_three_one, friday_three_two, friday_three_three, friday_three_four
                    await bot.send_message(message.from_user.id, f"1.{friday_three_one()}\n2.{friday_three_two()}\n3.{friday_three_three()}\n4.{thursday_three_four()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '4кл':
                    from schedule_xlrd import friday_four_one, friday_four_two, friday_four_three, friday_four_four, friday_four_five
                    await bot.send_message(message.from_user.id, f"1.{friday_four_one()}\n2.{friday_four_two()}\n3.{friday_four_three()}\n4.{friday_four_four()}\n5.{friday_four_five()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '5кл':
                    from schedule_xlrd import friday_five_one, friday_five_two, friday_five_three, friday_five_four, friday_five_five
                    await bot.send_message(message.from_user.id, f"1.{friday_five_one()}\n2.{friday_five_two()}\n3.{friday_five_three()}\n4.{friday_five_four()}\n5.{friday_five_five()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '6кл':
                    from schedule_xlrd import friday_six_one, friday_six_two, friday_six_three, friday_six_four, friday_six_five
                    await bot.send_message(message.from_user.id, f"1.{friday_six_one()}\n2.{friday_six_two()}\n3.{friday_six_three()}\n4.{friday_six_four()}\n5.{friday_six_five()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '7кл':
                    from schedule_xlrd import friday_seven_one, friday_seven_two, friday_seven_three, friday_seven_four, friday_seven_five
                    await bot.send_message(message.from_user.id, f"1.{friday_seven_one()}\n2.{friday_seven_two()}\n3.{friday_seven_three()}\n4.{friday_seven_four()}\n5.{friday_seven_five()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '8кл':
                    from schedule_xlrd import friday_eight_one, friday_eight_two, friday_eight_three, friday_eight_four, friday_eight_five, friday_eight_six
                    await bot.send_message(message.from_user.id, f"1.{friday_eight_one()}\n2.{friday_eight_two()}\n3.{friday_eight_three()}\n4.{friday_eight_four()}\n5.{friday_eight_five()}\n6.{friday_eight_six()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()
                
                case '9кл':
                    from schedule_xlrd import friday_nine_one, friday_nine_two, friday_nine_three, friday_nine_four, friday_nine_five, friday_nine_six, friday_nine_seven
                    await bot.send_message(message.from_user.id, f"1.{friday_nine_one()}\n2.{friday_nine_two()}\n3.{friday_nine_three()}\n4.{friday_nine_four()}\n5.{friday_nine_five()}\n6.{friday_nine_six()}\n7.{friday_nine_seven()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '10кл':
                    from schedule_xlrd import friday_ten_one, friday_ten_two, friday_ten_three ,friday_ten_four, friday_ten_five, friday_ten_six, friday_ten_seven
                    await bot.send_message(message.from_user.id, f"1.{friday_ten_one()}\n2.{friday_ten_two()}\n3.{friday_ten_three()}\n4.{friday_ten_four()}\n5.{friday_ten_five()}\n6.{friday_ten_six()}\n7.{friday_ten_seven()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '11кл':
                    from schedule_xlrd import friday_eleven_one, friday_eleven_two, friday_eleven_three, friday_eleven_four, friday_eleven_five, friday_eleven_six
                    await bot.send_message(message.from_user.id, f"1.{friday_eleven_one()}\n2.{friday_eleven_two()}\n3.{friday_eleven_three()}\n4.{friday_eleven_four()}\n5.{friday_eleven_five()}\n6.{friday_eleven_six()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()
            
        case 'Сб':
            match school_class:
                case '1кл':
                    from schedule_xlrd import sb_one
                    await bot.send_message(message.from_user.id, f"{sb_one()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '2кл':
                    from schedule_xlrd import sb_two
                    await bot.send_message(message.from_user.id, f"{sb_two()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '3кл':
                    from schedule_xlrd import sb_three
                    await bot.send_message(message.from_user.id, f"{sb_three()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '4кл':
                    from schedule_xlrd import sb_four
                    await bot.send_message(message.from_user.id, f"{sb_four()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '5кл':
                    from schedule_xlrd import sb_five
                    await bot.send_message(message.from_user.id, f"{sb_five()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '6кл':
                    from schedule_xlrd import sb_six
                    await bot.send_message(message.from_user.id, f"{sb_six()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '7кл':
                    from schedule_xlrd import sb_seven
                    await bot.send_message(message.from_user.id, f"{sb_seven()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '8кл':
                    from schedule_xlrd import sb_eight
                    await bot.send_message(message.from_user.id, f"{sb_eight()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '9кл':
                    from schedule_xlrd import sb_nine
                    await bot.send_message(message.from_user.id, f"{sb_nine()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()

                case '10кл':
                    from schedule_xlrd import sb_ten_time, sb_ten
                    await bot.send_message(message.from_user.id, f"Время: {sb_ten_time()}\nУрок: {sb_ten()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set()   

                case '11кл':
                    from schedule_xlrd import sb_eleven_time, sb_eleven
                    await bot.send_message(message.from_user.id, f"Время: {sb_eleven_time()}\nУрок: {sb_eleven()}", reply_markup=keyboard11)
                    await Schedule.choosing_school_day.set() 


        case 'Расписание звонков':
            await bot.send_message(message.from_user.id, "0 урок     08:05 - 08:50\n1 урок     09:00 - 09:45\
                \n2 урок     10:00 - 10:45\n3 урок     11:00 - 11:45\
                \n4 урок     12:00 - 12:45\n5 урок     13:05 - 13:50\n6 урок     14:10 - 14:55\
                \n7 урок     15:15 - 16:00", reply_markup=keyboard11)
            await Schedule.choosing_school_day.set()

        case 'Назад':
            await Schedule.choosing_school_class.set()
            kb = [
                [types.KeyboardButton(text="1кл"),
                types.KeyboardButton(text="2кл"),
                types.KeyboardButton(text="3кл")],
                [types.KeyboardButton(text="4кл"),
                types.KeyboardButton(text="5кл"),
                types.KeyboardButton(text="6кл")],
                [types.KeyboardButton(text="7кл"),
                types.KeyboardButton(text="8кл"),
                types.KeyboardButton(text="9кл")],
                [types.KeyboardButton(text="10кл"),
                types.KeyboardButton(text="Факультативы"),
                types.KeyboardButton(text="11кл")]
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="Выберите класс")
            await bot.send_message(message.from_user.id, 'Выбери класс', reply_markup=keyboard)
            @dp.message_handler(
                state = Schedule.choosing_school_class,
                text=avaliable_school_class
            ) 
            async def school_class(message: types.Message, state: FSMContext): 
                await state.update_data(chosen_school_class = message.text)
                user_data = await state.get_data()
                school_class = user_data['chosen_school_class']
                if school_class == "Факультативы":
                    kb1 = [
                        [types.KeyboardButton(text="Пн"),
                        types.KeyboardButton(text="Вт"),
                        types.KeyboardButton(text="Ср")],
                        [types.KeyboardButton(text="Чт"),
                        types.KeyboardButton(text="Пт"),
                        types.KeyboardButton(text="Сб")],
                        [types.KeyboardButton(text="Назад")]
                    ]
                    keyboard1 = types.ReplyKeyboardMarkup(keyboard=kb1, resize_keyboard=True, input_field_placeholder="Выберите день недели")
                    await bot.send_message (message.from_user.id, "Выбери день недели", reply_markup=keyboard1)
                    await state.finish()
                    await Facts.choosing_facts_day.set()

                    @dp.message_handler(
                    state=Facts.choosing_facts_day,
                    text = avaliable_facts_day
                    )   
                    async def fin_facts(message: types.Message, state: FSMContext):
                        await state.update_data(chosen_facts_day = message.text)
                        user_data = await state.get_data()
                        facts_day = user_data['chosen_facts_day']
                        match facts_day:
                            case 'Пн':
                                from facts import monday_prepod, monday_facult_name, monday_school_class, monday_time, monday_kab
                                await bot.send_message (message.from_user.id, f"Учитель: {monday_prepod()}\nЗанятие: {monday_facult_name()}\nКласс: {monday_school_class()}\nВремя: {monday_time()}\nКабинет: {monday_kab()}", reply_markup=keyboard1)

                            case'Вт':
                                from facts import tuesday_facult_name_one, tuesday_facult_name_three, tuesday_facult_name_two, tuesday_kab_one, tuesday_kab_three, tuesday_kab_two,\
                                    tuesday_prepod_one, tuesday_prepod_three, tuesday_prepod_two, tuesday_school_class_one,\
                                    tuesday_school_class_three, tuesday_school_class_two, tuesday_time_one, tuesday_time_three, tuesday_time_two
                                await bot.send_message (message.from_user.id, f"Учитель: {tuesday_prepod_one()}\nЗанятие: {tuesday_facult_name_one()}\nКласс: {tuesday_school_class_one()}\nВремя: {tuesday_time_one()}\nКабинет: {tuesday_kab_one()}", reply_markup=keyboard1)
                                await bot.send_message (message.from_user.id, f"Учитель: {tuesday_prepod_two()}\nЗанятие: {tuesday_facult_name_two()}\nКласс: {tuesday_school_class_two()}\nВремя: {tuesday_time_two()}\nКабинет: {tuesday_kab_two()}", reply_markup=keyboard1)
                                await bot.send_message (message.from_user.id, f"Учитель: {tuesday_prepod_three()}\nЗанятие: {tuesday_facult_name_three()}\nКласс: {tuesday_school_class_three()}\nВремя: {tuesday_time_three()}\nКабинет: {tuesday_kab_three()}", reply_markup=keyboard1)

                            case'Ср':
                                from facts import wensday_facult_name_one, wensday_facult_name_two, wensday_kab_one, wensday_kab_two, wensday_prepod_one,\
                                    wensday_prepod_two, wensday_school_class_one, wensday_school_class_two, wensday_time_one, wensday_time_two
                                await bot.send_message (message.from_user.id, f"Учитель: {wensday_prepod_one()}\nЗанятие: {wensday_facult_name_one()}\nКласс: {wensday_school_class_one()}\nВремя: {wensday_time_one()}\nКабинет: {wensday_kab_one()}", reply_markup=keyboard1)
                                await bot.send_message (message.from_user.id, f"Учитель: {wensday_prepod_two()}\nЗанятие: {wensday_facult_name_two()}\nКласс: {wensday_school_class_two()}\nВремя: {wensday_time_two()}\nКабинет: {wensday_kab_two()}", reply_markup=keyboard1)

                            case'Чт':
                                await bot.send_message (message.from_user.id, "Факультативов нету", reply_markup=keyboard1)

                            case'Пт':
                                from facts import friday_facult_name_four, friday_facult_name_one, friday_facult_name_three, friday_facult_name_two, friday_kab_four, friday_kab_one, friday_kab_three, friday_kab_two, friday_prepod_four, friday_prepod_one, friday_prepod_three,\
                                    friday_prepod_two, friday_school_class_four, friday_school_class_one, friday_school_class_three, friday_school_class_two, friday_time_four, friday_time_one, friday_time_three, friday_time_two
                                await bot.send_message (message.from_user.id, f"Учитель: {friday_prepod_one()}\nЗанятие: {friday_facult_name_one()}\nКласс: {friday_school_class_one()}\nВремя: {friday_time_one()}\nКабинет: {friday_kab_one()}", reply_markup=keyboard1)
                                await bot.send_message (message.from_user.id, f"Учитель: {friday_prepod_two()}\nЗанятие: {friday_facult_name_two()}\nКласс: {friday_school_class_two()}\nВремя: {friday_time_two()}\nКабинет: {friday_kab_two()}", reply_markup=keyboard1)
                                await bot.send_message (message.from_user.id, f"Учитель: {friday_prepod_three()}\nЗанятие: {friday_facult_name_three()}\nКласс: {friday_school_class_three()}\nВремя: {friday_time_three()}\nКабинет: {friday_kab_three()}", reply_markup=keyboard1)
                                await bot.send_message (message.from_user.id, f"Учитель: {friday_prepod_four()}\nЗанятие: {friday_facult_name_four()}\nКласс: {friday_school_class_four()}\nВремя: {friday_time_four()}\nКабинет: {friday_kab_four()}", reply_markup=keyboard1)

                            case'Сб':
                                from facts import saturday_facult_name_five, saturday_facult_name_four, saturday_facult_name_one, saturday_facult_name_three, saturday_facult_name_two, saturday_kab_five, saturday_kab_four, saturday_kab_one, saturday_kab_three, saturday_kab_two,\
                                    saturday_prepod_five, saturday_prepod_four, saturday_prepod_one, saturday_prepod_three, saturday_prepod_two, saturday_school_class_five, saturday_school_class_four, saturday_school_class_one, saturday_school_class_three, saturday_school_class_two,\
                                        saturday_time_five, saturday_time_four, saturday_time_one, saturday_time_three, saturday_time_two
                                await bot.send_message (message.from_user.id, f"Учитель: {saturday_prepod_one()}\nЗанятие: {saturday_facult_name_one()}\nКласс: {saturday_school_class_one()}\nВремя: {saturday_time_one()}\nКабинет: {saturday_kab_one()}", reply_markup=keyboard1)
                                await bot.send_message (message.from_user.id, f"Учитель: {saturday_prepod_two()}\nЗанятие: {saturday_facult_name_two()}\nКласс: {saturday_school_class_two()}\nВремя: {saturday_time_two()}\nКабинет: {saturday_kab_two()}", reply_markup=keyboard1)
                                await bot.send_message (message.from_user.id, f"Учитель: {saturday_prepod_three()}\nЗанятие: {saturday_facult_name_three()}\nКласс: {saturday_school_class_three()}\nВремя: {saturday_time_three()}\nКабинет: {saturday_kab_three()}", reply_markup=keyboard1)
                                await bot.send_message (message.from_user.id, f"Учитель: {saturday_prepod_four()}\nЗанятие: {saturday_facult_name_four()}\nКласс: {saturday_school_class_four()}\nВремя: {saturday_time_four()}\nКабинет: {saturday_kab_four()}", reply_markup=keyboard1)
                                await bot.send_message (message.from_user.id, f"Учитель: {saturday_prepod_five()}\nЗанятие: {saturday_facult_name_five()}\nКласс: {saturday_school_class_five()}\nВремя: {saturday_time_five()}\nКабинет: {saturday_kab_five()}", reply_markup=keyboard1)

                            case 'Назад':
                                await state.finish()
                                kb = [
                                [types.KeyboardButton(text="1кл"),
                                types.KeyboardButton(text="2кл"),
                                types.KeyboardButton(text="3кл")],
                                [types.KeyboardButton(text="4кл"),
                                types.KeyboardButton(text="5кл"),
                                types.KeyboardButton(text="6кл")],
                                [types.KeyboardButton(text="7кл"),
                                types.KeyboardButton(text="8кл"),
                                types.KeyboardButton(text="9кл")],
                                [types.KeyboardButton(text="10кл"),
                                types.KeyboardButton(text="Факультативы"),
                                types.KeyboardButton(text="11кл")]
                                ]
                                keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="Выберите класс")
                                await bot.send_message (message.from_user.id, "Вы вернулись назад", reply_markup=keyboard)
                                await Schedule.choosing_school_class.set()

                else:
                    kb1 = [
                        [types.KeyboardButton(text="Пн"),
                        types.KeyboardButton(text="Вт"),
                        types.KeyboardButton(text="Ср")],
                        [types.KeyboardButton(text="Чт"),
                        types.KeyboardButton(text="Пт"),
                        types.KeyboardButton(text="Сб")],
                        [types.KeyboardButton(text="Замены")]
                    ]
                    keyboard1 = types.ReplyKeyboardMarkup(keyboard=kb1, resize_keyboard=True, input_field_placeholder="Выберите день недели")
                    await bot.send_message (message.from_user.id, "Теперь выбери день недели", reply_markup=keyboard1)
                    await Schedule.next()
                    @dp.message_handler(
                        state=Schedule.choosing_school_day,
                        text = aviable_school_day
                    )   
                    async def finish(message: types.Message, state: FSMContext):
                        kb11 = [
                            [types.KeyboardButton(text="Пн"),
                            types.KeyboardButton(text="Вт"),
                            types.KeyboardButton(text="Ср")],
                            [types.KeyboardButton(text="Чт"),
                            types.KeyboardButton(text="Пт"),
                            types.KeyboardButton(text="Сб")],
                            [types.KeyboardButton(text="Расписание звонков"),
                            types.KeyboardButton(text="Замены")],
                            [types.KeyboardButton(text="Назад")]
                            ]
                        keyboard11 = types.ReplyKeyboardMarkup(keyboard=kb11, resize_keyboard=True)
                        await state.update_data(chosen_school_day = message.text)
                        user_data = await state.get_data()
                        school_class = user_data['chosen_school_class']
                        school_day = user_data['chosen_school_day']
                        match school_day:
                            case 'Пн':
                                match school_class:
                                    case "1кл":
                                        from schedule_xlrd import monday_one_one, monday_one_two, monday_one_three, monday_one_four
                                        await bot.send_message(message.from_user.id, f"1.{monday_one_one()}\n2.{monday_one_two()}\n3.{monday_one_three()}\n4.{monday_one_four()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()
                                        
                                    case "2кл":
                                        from schedule_xlrd import monday_two_one, monday_two_two, monday_two_three, monday_two_four
                                        await bot.send_message(message.from_user.id, f"1.{monday_two_one()}\n2.{monday_two_two()}\n3.{monday_two_three()}\n4.{monday_two_four()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case "3кл":
                                        from schedule_xlrd import monday_three_one, monday_three_two, monday_three_three, monday_three_four, monday_three_five
                                        await bot.send_message(message.from_user.id, f"1.{monday_three_one()}\n2.{monday_three_two()}\n3.{monday_three_three()}\n4.{monday_three_four()}\n5.{monday_three_five()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case "4кл":
                                        from schedule_xlrd import monday_four_one, monday_four_two, monday_four_three, monday_four_four
                                        await bot.send_message(message.from_user.id, f"1.{monday_four_one()}\n2.{monday_four_two()}\n3.{monday_four_three()}\n4.{monday_four_four()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case "5кл":
                                        from schedule_xlrd import monday_five_one, monday_five_two, monday_five_three, monday_five_four, monday_five_five, monday_five_six
                                        await bot.send_message(message.from_user.id, f"1.{monday_five_one()}\n2.{monday_five_two()}\n3.{monday_five_three()}\n4.{monday_five_four()}\n5.{monday_five_five()}\n6.{monday_five_six()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case "6кл":
                                        from schedule_xlrd import monday_six_one, monday_six_two, monday_six_three, monday_six_four, monday_six_five, monday_six_six
                                        await bot.send_message(message.from_user.id, f"1.{monday_six_one()}\n2.{monday_six_two()}\n3.{monday_six_three()}\n4.{monday_six_four()}\n5.{monday_six_five()}\n6.{monday_six_six()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case "7кл":
                                        from schedule_xlrd import monday_seven_one, monday_seven_two, monday_seven_three, monday_seven_four, monday_seven_five, monday_seven_six
                                        await bot.send_message(message.from_user.id, f"1.{monday_seven_one()}\n2.{monday_seven_two()}\n3.{monday_seven_three()}\n4.{monday_seven_four()}\n5.{monday_seven_five()}\n6.{monday_seven_six()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case "8кл":
                                        from schedule_xlrd import monday_eight_one, monday_eight_two, monday_eight_three, monday_eight_four, monday_eight_five, monday_eight_six, monday_eight_seven
                                        await bot.send_message(message.from_user.id, f"1.{monday_eight_one()}\n2.{monday_eight_two()}\n3.{monday_eight_three()}\n4.{monday_eight_four()}\n5.{monday_eight_five()}\n6.{monday_eight_six()}\n7.{monday_eight_seven()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case "9кл":
                                        from schedule_xlrd import monday_nine_one, monday_nine_two, monday_nine_three, monday_nine_four, monday_nine_five, monday_nine_six
                                        await bot.send_message(message.from_user.id, f"1.{monday_nine_one()}\n2.{monday_nine_two()}\n3.{monday_nine_three()}\n4.{monday_nine_four()}\n5.{monday_nine_five()}\n6.{monday_nine_six()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case "10кл":
                                        from schedule_xlrd import monday_ten_one, monday_ten_two, monday_ten_three, monday_ten_four, monday_ten_five, monday_ten_six
                                        await bot.send_message(message.from_user.id, f"1.{monday_ten_one()}\n2.{monday_ten_two()}\n3.{monday_ten_three()}\n4.{monday_ten_four()}\n5.{monday_ten_five()}\n6.{monday_ten_six()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case "11кл":
                                        from schedule_xlrd import monday_eleven_one, monday_eleven_two, monday_eleven_three, monday_eleven_four, monday_eleven_five, monday_eleven_six
                                        await bot.send_message(message.from_user.id, f"1.{monday_eleven_one()}\n2.{monday_eleven_two()}\n3.{monday_eleven_three()}\n4.{monday_eleven_four()}\n5.{monday_eleven_five()}\n6.{monday_eleven_six()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()
                                                                
                            case 'Вт':
                                match school_class:
                                    case "1кл":
                                        from schedule_xlrd import tuesday_one_one, tuesday_one_two, tuesday_one_three, tuesday_one_four
                                        await bot.send_message(message.from_user.id, f"1.{tuesday_one_one()}\n2.{tuesday_one_two()}\n3.{tuesday_one_three()}\n4.{tuesday_one_four()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case "2кл":
                                        from schedule_xlrd import tuesday_two_one, tuesday_two_two, tuesday_two_three, tuesday_two_four
                                        await bot.send_message(message.from_user.id, f"1.{tuesday_two_one()}\n2.{tuesday_two_two()}\n3.{tuesday_two_three()}\n4.{tuesday_two_four()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case "3кл":
                                        from  schedule_xlrd import tuesday_three_one, tuesday_three_two, tuesday_three_three, tuesday_three_four, tuesday_three_five
                                        await bot.send_message(message.from_user.id, f"1.{tuesday_three_one()}\n2.{tuesday_three_two()}\n3.{tuesday_three_three()}\n4.{tuesday_three_four()}\n5.{tuesday_three_five()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case "4кл":
                                        from schedule_xlrd import tuesday_four_one, tuesday_four_two, tuesday_four_three, tuesday_four_four, tuesday_four_five
                                        await bot.send_message(message.from_user.id, f"1.{tuesday_four_one()}\n2.{tuesday_four_two()}\n3.{tuesday_four_three()}\n4.{tuesday_four_four()}\n5.{tuesday_four_five()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case "5кл":
                                        from schedule_xlrd import tuesday_five_one, tuesday_five_two, tuesday_five_three, tuesday_five_four, tuesday_five_five, tuesday_five_six
                                        await bot.send_message(message.from_user.id, f"1.{tuesday_five_one()}\n2.{tuesday_five_two()}\n3.{tuesday_five_three()}\n4.{tuesday_five_four()}\n5.{tuesday_five_five()}\n6.{tuesday_five_six()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case "6кл":
                                        from schedule_xlrd import tuesday_six_one, tuesday_six_two, tuesday_six_three, tuesday_six_four, tuesday_six_five, tuesday_six_six
                                        await bot.send_message(message.from_user.id, f"1.{tuesday_six_one()}\n2.{tuesday_six_two()}\n3.{tuesday_six_three()}\n4.{tuesday_six_four()}\n5.{tuesday_six_five()}\n6.{tuesday_six_six()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case "7кл":
                                        from schedule_xlrd import tuesday_seven_one, tuesday_seven_two, tuesday_seven_three, tuesday_seven_four, tuesday_seven_five, tuesday_seven_six
                                        await bot.send_message(message.from_user.id, f"1.{tuesday_seven_one()}\n2.{tuesday_seven_two()}\n3.{tuesday_seven_three()}\n4.{tuesday_seven_four()}\n5.{tuesday_seven_five()}\n6.{tuesday_seven_six()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case "8кл":
                                        from schedule_xlrd import tuesday_eight_one, tuesday_eight_two, tuesday_eight_three, tuesday_eight_four, tuesday_eight_five, tuesday_eight_six
                                        await bot.send_message(message.from_user.id, f"1.{tuesday_eight_one()}\n2.{tuesday_eight_two()}\n3.{tuesday_eight_three()}\n4.{tuesday_eight_four()}\n5.{tuesday_eight_five()}\n6.{tuesday_eight_six()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case "9кл":
                                        from schedule_xlrd import tuesday_nine_one, tuesday_nine_two, tuesday_nine_three, tuesday_nine_four, tuesday_nine_five, tuesday_nine_six, tuesday_nine_seven
                                        await bot.send_message(message.from_user.id, f"1.{tuesday_nine_one()}\n2.{tuesday_nine_two()}\n3.{tuesday_nine_three()}\n4.{tuesday_nine_four()}\n5.{tuesday_nine_five()}\n6.{tuesday_nine_six()}\n7.{tuesday_nine_seven()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case "10кл":
                                        from schedule_xlrd import tuesday_ten_one, tuesday_ten_two, tuesday_ten_three, tuesday_ten_four, tuesday_ten_five, tuesday_ten_six
                                        await bot.send_message(message.from_user.id, f"1.{tuesday_ten_one()}\n2.{tuesday_ten_two()}\n3.{tuesday_ten_three()}\n4.{tuesday_ten_four()}\n5.{tuesday_ten_five()}\n6.{tuesday_ten_six()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case "11кл":
                                        from schedule_xlrd import tuesday_eleven_one, tuesday_eleven_two, tuesday_eleven_three, tuesday_eleven_four, tuesday_eleven_five, tuesday_eleven_six
                                        await bot.send_message(message.from_user.id, f"1.{tuesday_eleven_one()}\n2.{tuesday_eleven_two()}\n3.{tuesday_eleven_three()}\n4.{tuesday_eleven_four()}\n5.{tuesday_eleven_six()}\n6.{tuesday_eleven_two()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                            case 'Ср':
                                match school_class:
                                    case '1кл':
                                        from schedule_xlrd import wensday_one_one, wensday_one_two, wensday_one_three, wensday_one_four
                                        await bot.send_message(message.from_user.id, f"1.{wensday_one_one()}\n2.{wensday_one_two()}\n3.{wensday_one_three()}\n4.{wensday_one_four()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '2кл':
                                        from schedule_xlrd import wensday_two_one, wensday_two_two, wensday_two_three, wensday_two_four, wensday_two_five
                                        await bot.send_message(message.from_user.id, f"1.{wensday_two_one()}\n2.{wensday_two_two()}\n3.{wensday_two_three()}\n4.{wensday_two_four()}\n5.{wensday_two_five()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '3кл':
                                        from schedule_xlrd import wensday_three_one, wensday_three_two, wensday_three_three, wensday_three_four, wensday_three_five
                                        await bot.send_message(message.from_user.id, f"1.{wensday_three_one()}\n2.{wensday_three_two()}\n3.{wensday_three_three()}\n4.{wensday_three_four()}\n5.{wensday_three_five()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '4кл':
                                        from schedule_xlrd import wensday_four_one, wensday_four_two, wensday_four_three, wensday_four_four, wensday_four_five
                                        await bot.send_message(message.from_user.id, f"1.{wensday_four_one()}\n2.{wensday_four_two()}\n3.{wensday_four_three()}\n4.{wensday_four_four()}\n5.{wensday_four_five()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '5кл':
                                        from schedule_xlrd import wensday_five_one, wensday_five_two, wensday_five_three, wensday_five_four, wensday_five_five
                                        await bot.send_message(message.from_user.id, f"1.{wensday_five_one()}\n2.{wensday_five_two()}\n3.{wensday_five_three()}\n4.{wensday_five_four()}\n5.{wensday_five_five()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '6кл':
                                        from schedule_xlrd import wensday_six_one, wensday_six_two, wensday_six_three, wensday_six_four, wensday_six_five, wensday_six_six
                                        await bot.send_message(message.from_user.id, f"1.{wensday_six_one()}\n2.{wensday_six_two()}\n3.{wensday_six_three()}\n4.{wensday_six_four()}\n5.{wensday_six_five()}\n6.{wensday_six_six()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '7кл':
                                        from schedule_xlrd import wensday_seven_one, wensday_seven_two, wensday_seven_three, wensday_seven_four, wensday_seven_five, wensday_seven_six, wensday_seven_seven
                                        await bot.send_message(message.from_user.id, f"1.{wensday_seven_one()}\n2.{wensday_seven_two()}\n3.{wensday_seven_three()}\n4.{wensday_seven_four()}\n5.{wensday_seven_five()}\n6.{wensday_seven_six()}\n7.{wensday_seven_seven()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '8кл':
                                        from schedule_xlrd import wensday_eight_one, wensday_eight_two, wensday_eight_three, wensday_eight_four, wensday_eight_five, wensday_eight_six, wensday_eight_seven
                                        await bot.send_message(message.from_user.id, f"1.{wensday_eight_one()}\n2.{wensday_eight_two()}\n3.{wensday_eight_three()}\n4.{wensday_eight_four()}\n5.{wensday_eight_five()}\n6.{wensday_eight_six()}\n7.{wensday_eight_seven()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()
                                    
                                    case '9кл':
                                        from schedule_xlrd import wensday_nine_one, wensday_nine_two, wensday_nine_three, wensday_nine_four, wensday_nine_five, wensday_nine_six
                                        await bot.send_message(message.from_user.id, f"1.{wensday_nine_one()}\n2.{wensday_nine_two()}\n3.{wensday_nine_three()}\n4.{wensday_nine_four()}\n5.{wensday_nine_five()}\n6.{wensday_nine_six()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '10кл':
                                        from schedule_xlrd import wensday_ten_one, wensday_ten_two, wensday_ten_three, wensday_ten_four, wensday_ten_five, wensday_ten_six, wensday_ten_seven
                                        await bot.send_message(message.from_user.id, f"1.{wensday_ten_one()}\n2.{wensday_ten_two()}\n3.{wensday_ten_three()}\n4.{wensday_ten_four()}\n5.{wensday_ten_five()}\n6.{wensday_ten_six()}\n7.{wensday_ten_seven()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '11кл':
                                        from schedule_xlrd import wensday_eleven_one, wensday_eleven_two, wensday_eleven_three, wensday_eleven_four, wensday_eleven_five, wensday_eleven_six, wensday_eleven_seven
                                        await bot.send_message(message.from_user.id, f"1.{wensday_eleven_one()}\n2.{wensday_eleven_two()}\n3.{wensday_eleven_three()}\n4.{wensday_eleven_four()}\n5.{wensday_eleven_five()}\n6.{wensday_eleven_six()}\n7.{wensday_eleven_seven()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                            case 'Чт':
                                match school_class:
                                    case '1кл':
                                        from schedule_xlrd import thursday_one_one, thursday_one_two, thursday_one_three
                                        await bot.send_message(message.from_user.id, f"1.{thursday_one_one()}\n2.{thursday_one_two()}\n3.{thursday_one_three()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '2кл':
                                        from schedule_xlrd import thursday_two_one, thursday_two_two, thursday_two_three, thursday_two_four
                                        await bot.send_message(message.from_user.id, f"1.{thursday_two_one()}\n2.{thursday_two_two()}\n3.{thursday_two_three()}\n4.{thursday_two_four()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '3кл':
                                        from schedule_xlrd import thursday_three_one, thursday_three_two, thursday_three_three, thursday_three_four, thursday_three_five
                                        await bot.send_message(message.from_user.id, f"1.{thursday_three_one()}\n2.{thursday_three_two()}\n3.{thursday_three_three()}\n4.{thursday_three_four()}\n5.{thursday_three_five()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '4кл':
                                        from schedule_xlrd import thursday_four_one, thursday_four_two, thursday_four_three, thursday_four_four,thursday_four_five
                                        await bot.send_message(message.from_user.id, f"1.{thursday_four_one()}\n2.{thursday_four_two()}\n3.{thursday_four_three()}\n4.{thursday_four_four()}\n5.{thursday_four_five()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '5кл':
                                        from schedule_xlrd import thursday_five_one, thursday_five_two, thursday_five_three, thursday_five_four, thursday_five_five
                                        await bot.send_message(message.from_user.id, f"1.{thursday_five_one()}\n2.{thursday_five_two()}\n3.{thursday_five_three()}\n4.{thursday_five_four()}\n5.{thursday_five_five()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '6кл':
                                        from schedule_xlrd import thursday_six_one, thursday_six_two, thursday_six_three, thursday_six_four, thursday_six_five
                                        await bot.send_message(message.from_user.id, f"1.{thursday_six_one()}\n2.{thursday_six_two()}\n3.{thursday_six_three()}\n4.{thursday_six_four()}\n5.{thursday_six_five()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '7кл':
                                        from schedule_xlrd import thursday_seven_one, thursday_seven_two, thursday_seven_three, thursday_seven_four, thursday_seven_five, thursday_seven_six
                                        await bot.send_message(message.from_user.id, f"1.{thursday_seven_one()}\n2.{thursday_seven_two()}\n3.{thursday_seven_three()}\n4.{thursday_seven_four()}\n5.{thursday_seven_five()}\n6.{thursday_seven_six()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '8кл':
                                        from schedule_xlrd import thursday_eight_one, thursday_eight_two, thursday_eight_three, thursday_eight_four, thursday_eight_five, thursday_eight_six
                                        await bot.send_message(message.from_user.id, f"1.{thursday_eight_one()}\n2.{thursday_eight_two()}\n3.{thursday_eight_three()}\n4.{thursday_eight_four()}\n5.{thursday_eight_five()}\n6.{thursday_eight_six()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()
                                    
                                    case '9кл':
                                        from schedule_xlrd import thursday_nine_one, thursday_nine_two, thursday_nine_three, thursday_nine_four, thursday_nine_five, thursday_nine_six
                                        await bot.send_message(message.from_user.id, f"1.{thursday_nine_one()}\n2.{thursday_nine_two()}\n3.{thursday_nine_three()}\n4.{thursday_nine_four()}\n5.{thursday_nine_five()}\n6.{thursday_nine_six()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '10кл':
                                        from schedule_xlrd import thursday_ten_one, thursday_ten_two, thursday_ten_three, thursday_ten_four, thursday_ten_five, thursday_ten_six
                                        await bot.send_message(message.from_user.id, f"1.{thursday_ten_one()}\n2.{thursday_ten_two()}\n3.{thursday_ten_three()}\n4.{thursday_ten_four()}\n5.{thursday_ten_five()}\n6.{thursday_ten_six()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '11кл':
                                        from schedule_xlrd import thursday_eleven_one, thursday_eleven_two, thursday_eleven_three, thursday_eleven_four, thursday_eleven_five, thursday_eleven_six, thursday_eleven_seven
                                        await bot.send_message(message.from_user.id, f"1.{thursday_eleven_one()}\n2.{thursday_eleven_two()}\n3.{thursday_eleven_three()}\n4.{thursday_eleven_four()}\n5.{thursday_eleven_five()}\n6.{thursday_eleven_six()}\n7.{thursday_eleven_seven()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()
                                
                            case 'Пт':
                                match school_class:
                                    case '1кл':
                                        from schedule_xlrd import friday_one_one, friday_one_two, friday_one_three, monday_one_four
                                        await bot.send_message(message.from_user.id, f"1.{friday_one_one()}\n2.{friday_one_two()}\n3.{friday_one_three()}\n4.{monday_one_four()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '2кл':
                                        from schedule_xlrd import friday_two_one, friday_two_two, friday_two_three, friday_two_four
                                        await bot.send_message(message.from_user.id, f"1.{friday_two_one()}\n2.{friday_two_two()}\n3.{friday_two_three()}\n4.{friday_two_four()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '3кл':
                                        from schedule_xlrd import friday_three_one, friday_three_two, friday_three_three, friday_three_four
                                        await bot.send_message(message.from_user.id, f"1.{friday_three_one()}\n2.{friday_three_two()}\n3.{friday_three_three()}\n4.{thursday_three_four()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '4кл':
                                        from schedule_xlrd import friday_four_one, friday_four_two, friday_four_three, friday_four_four, friday_four_five
                                        await bot.send_message(message.from_user.id, f"1.{friday_four_one()}\n2.{friday_four_two()}\n3.{friday_four_three()}\n4.{friday_four_four()}\n5.{friday_four_five()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '5кл':
                                        from schedule_xlrd import friday_five_one, friday_five_two, friday_five_three, friday_five_four, friday_five_five
                                        await bot.send_message(message.from_user.id, f"1.{friday_five_one()}\n2.{friday_five_two()}\n3.{friday_five_three()}\n4.{friday_five_four()}\n5.{friday_five_five()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '6кл':
                                        from schedule_xlrd import friday_six_one, friday_six_two, friday_six_three, friday_six_four, friday_six_five
                                        await bot.send_message(message.from_user.id, f"1.{friday_six_one()}\n2.{friday_six_two()}\n3.{friday_six_three()}\n4.{friday_six_four()}\n5.{friday_six_five()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '7кл':
                                        from schedule_xlrd import friday_seven_one, friday_seven_two, friday_seven_three, friday_seven_four, friday_seven_five
                                        await bot.send_message(message.from_user.id, f"1.{friday_seven_one()}\n2.{friday_seven_two()}\n3.{friday_seven_three()}\n4.{friday_seven_four()}\n5.{friday_seven_five()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '8кл':
                                        from schedule_xlrd import friday_eight_one, friday_eight_two, friday_eight_three, friday_eight_four, friday_eight_five, friday_eight_six
                                        await bot.send_message(message.from_user.id, f"1.{friday_eight_one()}\n2.{friday_eight_two()}\n3.{friday_eight_three()}\n4.{friday_eight_four()}\n5.{friday_eight_five()}\n6.{friday_eight_six()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()
                                    
                                    case '9кл':
                                        from schedule_xlrd import friday_nine_one, friday_nine_two, friday_nine_three, friday_nine_four, friday_nine_five, friday_nine_six, friday_nine_seven
                                        await bot.send_message(message.from_user.id, f"1.{friday_nine_one()}\n2.{friday_nine_two()}\n3.{friday_nine_three()}\n4.{friday_nine_four()}\n5.{friday_nine_five()}\n6.{friday_nine_six()}\n7.{friday_nine_seven()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '10кл':
                                        from schedule_xlrd import friday_ten_one, friday_ten_two, friday_ten_three ,friday_ten_four, friday_ten_five, friday_ten_six, friday_ten_seven
                                        await bot.send_message(message.from_user.id, f"1.{friday_ten_one()}\n2.{friday_ten_two()}\n3.{friday_ten_three()}\n4.{friday_ten_four()}\n5.{friday_ten_five()}\n6.{friday_ten_six()}\n7.{friday_ten_seven()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '11кл':
                                        from schedule_xlrd import friday_eleven_one, friday_eleven_two, friday_eleven_three, friday_eleven_four, friday_eleven_five, friday_eleven_six
                                        await bot.send_message(message.from_user.id, f"1.{friday_eleven_one()}\n2.{friday_eleven_two()}\n3.{friday_eleven_three()}\n4.{friday_eleven_four()}\n5.{friday_eleven_five()}\n6.{friday_eleven_six()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()
                                
                            case 'Сб':
                                match school_class:
                                    case '1кл':
                                        from schedule_xlrd import sb_one
                                        await bot.send_message(message.from_user.id, f"{sb_one()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '2кл':
                                        from schedule_xlrd import sb_two
                                        await bot.send_message(message.from_user.id, f"{sb_two()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '3кл':
                                        from schedule_xlrd import sb_three
                                        await bot.send_message(message.from_user.id, f"{sb_three()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '4кл':
                                        from schedule_xlrd import sb_four
                                        await bot.send_message(message.from_user.id, f"{sb_four()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '5кл':
                                        from schedule_xlrd import sb_five
                                        await bot.send_message(message.from_user.id, f"{sb_five()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '6кл':
                                        from schedule_xlrd import sb_six
                                        await bot.send_message(message.from_user.id, f"{sb_six()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '7кл':
                                        from schedule_xlrd import sb_seven
                                        await bot.send_message(message.from_user.id, f"{sb_seven()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '8кл':
                                        from schedule_xlrd import sb_eight
                                        await bot.send_message(message.from_user.id, f"{sb_eight()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '9кл':
                                        from schedule_xlrd import sb_nine
                                        await bot.send_message(message.from_user.id, f"{sb_nine()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()

                                    case '10кл':
                                        from schedule_xlrd import sb_ten_time, sb_ten
                                        await bot.send_message(message.from_user.id, f"Время: {sb_ten_time()}\nУрок: {sb_ten()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set()   

                                    case '11кл':
                                        from schedule_xlrd import sb_eleven_time, sb_eleven
                                        await bot.send_message(message.from_user.id, f"Время: {sb_eleven_time()}\nУрок: {sb_eleven()}", reply_markup=keyboard11)
                                        await Schedule.choosing_school_day.set() 
                            
        case 'Замены':
            from zam import availability, availability_one, availability_two, availability_three, availability_four, availability_five, availability_six, availability_seven, availability_eight, availability_nine, availability_ten, availability_eleven
            if availability() == 'tr':
                match school_class:
                    case '1кл':
                        if availability_one() == 'tr':
                            from zam import one_one, one_two, one_three, one_four, one_five, one_six, one_one_test, one_two_test, one_three_test, one_four_test, one_five_test, one_six_test
                            if one_one_test() == 't' and one_two_test() == 't' and one_three_test() == 't' and one_four_test() == 't' and one_five_test() == 't' and one_six_test() == 't':
                                await bot.send_message(message.from_user.id, f"{one_one()}\n{one_two()}\n{one_three()}\n{one_four()}\n{one_five()}\n{one_six()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                                
                            elif one_one_test() == 't' and one_two_test() == 't' and one_three_test() == 't' and one_four_test() == 't' and one_five_test() == 't':
                                await bot.send_message(message.from_user.id, f"{one_one()}\n{one_two()}\n{one_three()}\n{one_four()}\n{one_five()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()

                            elif one_one_test() == 't' and one_two_test() == 't' and one_three_test() == 't' and one_four_test() == 't':
                                await bot.send_message(message.from_user.id, f"{one_one()}\n{one_two()}\n{one_three()}\n{one_four()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()

                            elif one_one_test() == 't' and one_two_test() == 't' and one_three_test() == 't':
                                await bot.send_message(message.from_user.id, f"{one_one()}\n{one_two()}\n{one_three()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                            
                            elif one_one_test() == 't' and one_two_test() == 't':
                                await bot.send_message(message.from_user.id, f"{one_one()}\n{one_two()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                            
                            elif one_one_test() == 't':
                                await bot.send_message(message.from_user.id, f"{one_one()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                            
                        else:
                            await bot.send_message(message.from_user.id, "Список замен пуст", reply_markup=keyboard11) 
                            await Schedule.choosing_school_day.set()
                    
                    case '2кл':
                        if availability_two() == 'tr':
                            from zam import two_one, two_two, two_three, two_four, two_five, two_six, two_one_test, two_two_test, two_three_test, two_four_test, two_five_test, two_six_test
                            if two_one_test() == 't' and two_two_test() == 't' and two_three_test() == 't' and two_four_test() == 't' and two_five_test() == 't' and two_six_test() == 't':
                                await bot.send_message(message.from_user.id, f"{two_one()}\n{two_two()}\n{two_three()}\n{two_four()}\n{two_five()}\n{two_six()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                                
                            elif two_one_test() == 't' and two_two_test() == 't' and two_three_test() == 't' and two_four_test() == 't' and two_five_test() == 't':
                                await bot.send_message(message.from_user.id, f"{two_one()}\n{two_two()}\n{two_three()}\n{two_four()}\n{two_five()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()

                            elif two_one_test() == 't' and two_two_test() == 't' and two_three_test() == 't' and two_four_test() == 't':
                                await bot.send_message(message.from_user.id, f"{two_one()}\n{two_two()}\n{two_three()}\n{two_four()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()

                            elif two_one_test() == 't' and two_two_test() == 't' and two_three_test() == 't':
                                await bot.send_message(message.from_user.id, f"{two_one()}\n{two_two()}\n{two_three()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                            
                            elif two_one_test() == 't' and two_two_test() == 't':
                                await bot.send_message(message.from_user.id, f"{two_one()}\n{two_two()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                            
                            elif two_one_test() == 't':
                                await bot.send_message(message.from_user.id, f"{two_one()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                        else:
                            await bot.send_message(message.from_user.id, "Список замен пуст", reply_markup=keyboard11) 
                            await Schedule.choosing_school_day.set()
                    
                    case '3кл':
                        if availability_three() == 'tr':
                            from zam import three_one, three_two, three_three, three_four, three_five, three_six, three_one_test, three_two_test, three_three_test, three_four_test, three_five_test, three_six_test
                            if three_one_test() == 't' and three_two_test() == 't' and three_three_test() == 't' and three_four_test() == 't' and three_five_test() == 't' and three_six_test() == 't':
                                await bot.send_message(message.from_user.id, f"{three_one()}\n{three_two()}\n{three_three()}\n{three_four()}\n{three_five()}\n{three_six()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                                
                            elif three_one_test() == 't' and three_two_test() == 't' and three_three_test() == 't' and three_four_test() == 't' and three_five_test() == 't':
                                await bot.send_message(message.from_user.id, f"{three_one()}\n{three_two()}\n{three_three()}\n{three_four()}\n{three_five()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()

                            elif three_one_test() == 't' and three_two_test() == 't' and three_three_test() == 't' and three_four_test() == 't':
                                await bot.send_message(message.from_user.id, f"{three_one()}\n{three_two()}\n{three_three()}\n{three_four()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()

                            elif three_one_test() == 't' and three_two_test() == 't' and three_three_test() == 't':
                                await bot.send_message(message.from_user.id, f"{three_one()}\n{three_two()}\n{three_three()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                            
                            elif three_one_test() == 't' and three_two_test() == 't':
                                await bot.send_message(message.from_user.id, f"{three_one()}\n{three_two()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                            
                            elif three_one_test() == 't':
                                await bot.send_message(message.from_user.id, f"{three_one()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                            
                        else:
                            await bot.send_message(message.from_user.id, "Список замен пуст", reply_markup=keyboard11) 
                            await Schedule.choosing_school_day.set()    
                    
                    case '4кл':
                        if availability_four() == 'tr':
                            from zam import four_one, four_two, four_three, four_four, four_five, four_six, four_one_test, four_two_test, four_three_test, four_four_test, four_five_test, four_six_test
                            if four_one_test() == 't' and four_two_test() == 't' and four_three_test() == 't' and four_four_test() == 't' and four_five_test() == 't' and four_six_test() == 't':
                                await bot.send_message(message.from_user.id, f"{four_one()}\n{four_two()}\n{four_three()}\n{four_four()}\n{four_five()}\n{four_six()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                                
                            elif four_one_test() == 't' and four_two_test() == 't' and four_three_test() == 't' and four_four_test() == 't' and four_five_test() == 't':
                                await bot.send_message(message.from_user.id, f"{four_one()}\n{four_two()}\n{four_three()}\n{four_four()}\n{four_five()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()

                            elif four_one_test() == 't' and four_two_test() == 't' and four_three_test() == 't' and four_four_test() == 't':
                                await bot.send_message(message.from_user.id, f"{four_one()}\n{four_two()}\n{four_three()}\n{four_four()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()

                            elif four_one_test() == 't' and four_two_test() == 't' and four_three_test() == 't':
                                await bot.send_message(message.from_user.id, f"{four_one()}\n{four_two()}\n{four_three()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                            
                            elif four_one_test() == 't' and four_two_test() == 't':
                                await bot.send_message(message.from_user.id, f"{four_one()}\n{four_two()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                            
                            elif four_one_test() == 't':
                                await bot.send_message(message.from_user.id, f"{four_one()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                        
                        else:
                            await bot.send_message(message.from_user.id, "Список замен пуст", reply_markup=keyboard11) 
                            await Schedule.choosing_school_day.set()
                    
                    case '5кл':
                        if availability_five() == 'tr':
                            from zam import five_one, five_two, five_three, five_four, five_five, five_six, five_seven, five_one_test, five_two_test, five_three_test, five_four_test, five_five_test, five_six_test, five_seven_test
                            if five_one_test() == 't' and five_two_test() == 't' and five_three_test() == 't' and five_four_test() == 't' and five_five_test() == 't' and five_six_test() == 't' and five_seven_test() == 't':
                                await bot.send_message(message.from_user.id, f"{five_one()}\n{five_two()}\n{five_three()}\n{five_four()}\n{five_five()}\n{five_six()}\n{five_seven()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()

                            elif five_one_test() == 't' and five_two_test() == 't' and five_three_test() == 't' and five_four_test() == 't' and five_five_test() == 't' and five_six_test() == 't':
                                await bot.send_message(message.from_user.id, f"{five_one()}\n{five_two()}\n{five_three()}\n{five_four()}\n{five_five()}\n{five_six()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                                
                            elif five_one_test() == 't' and five_two_test() == 't' and five_three_test() == 't' and five_four_test() == 't' and five_five_test() == 't':
                                await bot.send_message(message.from_user.id, f"{five_one()}\n{five_two()}\n{five_three()}\n{five_four()}\n{five_five()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()

                            elif five_one_test() == 't' and five_two_test() == 't' and five_three_test() == 't' and five_four_test() == 't':
                                await bot.send_message(message.from_user.id, f"{five_one()}\n{five_two()}\n{five_three()}\n{five_four()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()

                            elif five_one_test() == 't' and five_two_test() == 't' and five_three_test() == 't':
                                await bot.send_message(message.from_user.id, f"{five_one()}\n{five_two()}\n{five_three()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                            
                            elif five_one_test() == 't' and five_two_test() == 't':
                                await bot.send_message(message.from_user.id, f"{five_one()}\n{five_two()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                            
                            elif five_one_test() == 't':
                                await bot.send_message(message.from_user.id, f"{five_one()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                        
                        else:
                            await bot.send_message(message.from_user.id, "Список замен пуст", reply_markup=keyboard11) 
                            await Schedule.choosing_school_day.set()
                    
                    case '6кл':
                        if availability_six() == 'tr':
                            from zam import six_one, six_two, six_three, six_four, six_five, six_six, six_seven, six_one_test, six_two_test, six_three_test, six_four_test, six_five_test, six_six_test, six_seven_test
                            if six_one_test() == 't' and six_two_test() == 't' and six_three_test() == 't' and six_four_test() == 't' and six_five_test() == 't' and six_six_test() == 't' and six_seven_test() == 't':
                                await bot.send_message(message.from_user.id, f"{six_one()}\n{six_two()}\n{six_three()}\n{six_four()}\n{six_five()}\n{six_six()}\n{six_seven()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()

                            elif six_one_test() == 't' and six_two_test() == 't' and six_three_test() == 't' and six_four_test() == 't' and six_five_test() == 't' and six_six_test() == 't':
                                await bot.send_message(message.from_user.id, f"{six_one()}\n{six_two()}\n{six_three()}\n{six_four()}\n{six_five()}\n{six_six()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                                
                            elif six_one_test() == 't' and six_two_test() == 't' and six_three_test() == 't' and six_four_test() == 't' and six_five_test() == 't':
                                await bot.send_message(message.from_user.id, f"{six_one()}\n{six_two()}\n{six_three()}\n{six_four()}\n{six_five()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()

                            elif six_one_test() == 't' and six_two_test() == 't' and six_three_test() == 't' and six_four_test() == 't':
                                await bot.send_message(message.from_user.id, f"{six_one()}\n{six_two()}\n{six_three()}\n{six_four()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()

                            elif six_one_test() == 't' and six_two_test() == 't' and six_three_test() == 't':
                                await bot.send_message(message.from_user.id, f"{six_one()}\n{six_two()}\n{six_three()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                            
                            elif six_one_test() == 't' and six_two_test() == 't':
                                await bot.send_message(message.from_user.id, f"{six_one()}\n{six_two()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                            
                            elif six_one_test() == 't':
                                await bot.send_message(message.from_user.id, f"{six_one()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                        
                        else:
                            await bot.send_message(message.from_user.id, "Список замен пуст", reply_markup=keyboard11) 
                            await Schedule.choosing_school_day.set()
                    
                    case '7кл':
                        if availability_seven() == 'tr':
                            from zam import seven_one, seven_two, seven_three, seven_four, seven_five, seven_six, seven_seven, seven_one_test, seven_two_test, seven_three_test, seven_four_test, seven_five_test, seven_six_test, seven_seven_test
                            if seven_one_test() == 't' and seven_two_test() == 't' and seven_three_test() == 't' and seven_four_test() == 't' and seven_five_test() == 't' and seven_six_test() == 't' and seven_seven_test() == 't':
                                await bot.send_message(message.from_user.id, f"{seven_one()}\n{seven_two()}\n{seven_three()}\n{seven_four()}\n{seven_five()}\n{seven_six()}\n{seven_seven()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()

                            elif seven_one_test() == 't' and seven_two_test() == 't' and seven_three_test() == 't' and seven_four_test() == 't' and seven_five_test() == 't' and seven_six_test() == 't':
                                await bot.send_message(message.from_user.id, f"{seven_one()}\n{seven_two()}\n{seven_three()}\n{seven_four()}\n{seven_five()}\n{seven_six()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                                
                            elif seven_one_test() == 't' and seven_two_test() == 't' and seven_three_test() == 't' and seven_four_test() == 't' and seven_five_test() == 't':
                                await bot.send_message(message.from_user.id, f"{seven_one()}\n{seven_two()}\n{seven_three()}\n{seven_four()}\n{seven_five()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()

                            elif seven_one_test() == 't' and seven_two_test() == 't' and seven_three_test() == 't' and seven_four_test() == 't':
                                await bot.send_message(message.from_user.id, f"{seven_one()}\n{seven_two()}\n{seven_three()}\n{seven_four()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()

                            elif seven_one_test() == 't' and seven_two_test() == 't' and seven_three_test() == 't':
                                await bot.send_message(message.from_user.id, f"{seven_one()}\n{seven_two()}\n{seven_three()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                            
                            elif seven_one_test() == 't' and seven_two_test() == 't':
                                await bot.send_message(message.from_user.id, f"{seven_one()}\n{seven_two()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                            
                            elif seven_one_test() == 't':
                                await bot.send_message(message.from_user.id, f"{seven_one()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                        
                        else:
                            await bot.send_message(message.from_user.id, "Список замен пуст", reply_markup=keyboard11) 
                            await Schedule.choosing_school_day.set()
                    
                    case '8кл':
                        if availability_eight() == 'tr':
                            from zam import eight_one, eight_two, eight_three, eight_four, eight_five, eight_six, eight_seven, eight_one_test, eight_two_test, eight_three_test, eight_four_test, eight_five_test, eight_six_test, eight_seven_test
                            if eight_one_test() == 't' and eight_two_test() == 't' and eight_three_test() == 't' and eight_four_test() == 't' and eight_five_test() == 't' and eight_six_test() == 't' and eight_seven_test() == 't':
                                await bot.send_message(message.from_user.id, f"{eight_one()}\n{eight_two()}\n{eight_three()}\n{eight_four()}\n{eight_five()}\n{eight_six()}\n{eight_seven()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()

                            elif eight_one_test() == 't' and eight_two_test() == 't' and eight_three_test() == 't' and eight_four_test() == 't' and eight_five_test() == 't' and eight_six_test() == 't':
                                await bot.send_message(message.from_user.id, f"{eight_one()}\n{eight_two()}\n{eight_three()}\n{eight_four()}\n{eight_five()}\n{eight_six()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                                
                            elif eight_one_test() == 't' and eight_two_test() == 't' and eight_three_test() == 't' and eight_four_test() == 't' and eight_five_test() == 't':
                                await bot.send_message(message.from_user.id, f"{eight_one()}\n{eight_two()}\n{eight_three()}\n{eight_four()}\n{eight_five()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()

                            elif eight_one_test() == 't' and eight_two_test() == 't' and eight_three_test() == 't' and eight_four_test() == 't':
                                await bot.send_message(message.from_user.id, f"{eight_one()}\n{eight_two()}\n{eight_three()}\n{eight_four()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()

                            elif eight_one_test() == 't' and eight_two_test() == 't' and eight_three_test() == 't':
                                await bot.send_message(message.from_user.id, f"{eight_one()}\n{eight_two()}\n{eight_three()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                            
                            elif eight_one_test() == 't' and eight_two_test() == 't':
                                await bot.send_message(message.from_user.id, f"{eight_one()}\n{eight_two()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                            
                            elif eight_one_test() == 't':
                                await bot.send_message(message.from_user.id, f"{eight_one()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                        
                        else:
                            await bot.send_message(message.from_user.id, "Список замен пуст", reply_markup=keyboard11) 
                            await Schedule.choosing_school_day.set()
                    
                    case '9кл':
                        if availability_nine() == 'tr':
                            from zam import nine_one, nine_two, nine_three, nine_four, nine_five, nine_six, nine_seven, nine_one_test, nine_two_test, nine_three_test, nine_four_test, nine_five_test, nine_six_test, nine_seven_test
                            if nine_one_test() == 't' and nine_two_test() == 't' and nine_three_test() == 't' and nine_four_test() == 't' and nine_five_test() == 't' and nine_six_test() == 't' and nine_seven_test() == 't':
                                await bot.send_message(message.from_user.id, f"{nine_one()}\n{nine_two()}\n{nine_three()}\n{nine_four()}\n{nine_five()}\n{nine_six()}\n{nine_seven()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()

                            elif nine_one_test() == 't' and nine_two_test() == 't' and nine_three_test() == 't' and nine_four_test() == 't' and nine_five_test() == 't' and nine_six_test() == 't':
                                await bot.send_message(message.from_user.id, f"{nine_one()}\n{nine_two()}\n{nine_three()}\n{nine_four()}\n{nine_five()}\n{nine_six()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                                
                            elif nine_one_test() == 't' and nine_two_test() == 't' and nine_three_test() == 't' and nine_four_test() == 't' and nine_five_test() == 't':
                                await bot.send_message(message.from_user.id, f"{nine_one()}\n{nine_two()}\n{nine_three()}\n{nine_four()}\n{nine_five()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()

                            elif nine_one_test() == 't' and nine_two_test() == 't' and nine_three_test() == 't' and nine_four_test() == 't':
                                await bot.send_message(message.from_user.id, f"{nine_one()}\n{nine_two()}\n{nine_three()}\n{nine_four()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()

                            elif nine_one_test() == 't' and nine_two_test() == 't' and nine_three_test() == 't':
                                await bot.send_message(message.from_user.id, f"{nine_one()}\n{nine_two()}\n{nine_three()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                            
                            elif nine_one_test() == 't' and nine_two_test() == 't':
                                await bot.send_message(message.from_user.id, f"{nine_one()}\n{nine_two()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                            
                            elif nine_one_test() == 't':
                                await bot.send_message(message.from_user.id, f"{nine_one()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                        
                        else:
                            await bot.send_message(message.from_user.id, "Список замен пуст", reply_markup=keyboard11) 
                            await Schedule.choosing_school_day.set()
                        
                    case '10кл':
                        if availability_ten() == 'tr':
                            from zam import ten_one, ten_two, ten_three, ten_four, ten_five, ten_six, ten_seven, ten_one_test, ten_two_test, ten_three_test, ten_four_test, ten_five_test, ten_six_test, ten_seven_test
                            if ten_one_test() == 't' and ten_two_test() == 't' and ten_three_test() == 't' and ten_four_test() == 't' and ten_five_test() == 't' and ten_six_test() == 't' and ten_seven_test() == 't':
                                await bot.send_message(message.from_user.id, f"{ten_one()}\n{ten_two()}\n{ten_three()}\n{ten_four()}\n{ten_five()}\n{ten_six()}\n{ten_seven()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()

                            elif ten_one_test() == 't' and ten_two_test() == 't' and ten_three_test() == 't' and ten_four_test() == 't' and ten_five_test() == 't' and ten_six_test() == 't':
                                await bot.send_message(message.from_user.id, f"{ten_one()}\n{ten_two()}\n{ten_three()}\n{ten_four()}\n{ten_five()}\n{ten_six()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                                
                            elif ten_one_test() == 't' and ten_two_test() == 't' and ten_three_test() == 't' and ten_four_test() == 't' and ten_five_test() == 't':
                                await bot.send_message(message.from_user.id, f"{ten_one()}\n{ten_two()}\n{ten_three()}\n{ten_four()}\n{ten_five()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()

                            elif ten_one_test() == 't' and ten_two_test() == 't' and ten_three_test() == 't' and ten_four_test() == 't':
                                await bot.send_message(message.from_user.id, f"{ten_one()}\n{ten_two()}\n{ten_three()}\n{ten_four()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()

                            elif ten_one_test() == 't' and ten_two_test() == 't' and ten_three_test() == 't':
                                await bot.send_message(message.from_user.id, f"{ten_one()}\n{ten_two()}\n{ten_three()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                            
                            elif ten_one_test() == 't' and ten_two_test() == 't':
                                await bot.send_message(message.from_user.id, f"{ten_one()}\n{ten_two()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                            
                            elif ten_one_test() == 't':
                                await bot.send_message(message.from_user.id, f"{ten_one()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                        
                        else:
                            await bot.send_message(message.from_user.id, "Список замен пуст", reply_markup=keyboard11) 
                            await Schedule.choosing_school_day.set()
                    
                    case '11кл':
                        if availability_eleven() == 'tr':
                            from zam import eleven_one, eleven_two, eleven_three, eleven_four, eleven_five, eleven_six, eleven_seven, eleven_one_test, eleven_two_test, eleven_three_test, eleven_four_test, eleven_five_test, eleven_six_test, eleven_seven_test
                            if eleven_one_test() == 't' and eleven_two_test() == 't' and eleven_three_test() == 't' and eleven_four_test() == 't' and eleven_five_test() == 't' and eleven_six_test() == 't' and eleven_seven_test() == 't':
                                await bot.send_message(message.from_user.id, f"{eleven_one()}\n{eleven_two()}\n{eleven_three()}\n{eleven_four()}\n{eleven_five()}\n{eleven_six()}\n{eleven_seven()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()

                            elif eleven_one_test() == 't' and eleven_two_test() == 't' and eleven_three_test() == 't' and eleven_four_test() == 't' and eleven_five_test() == 't' and eleven_six_test() == 't':
                                await bot.send_message(message.from_user.id, f"{eleven_one()}\n{eleven_two()}\n{eleven_three()}\n{eleven_four()}\n{eleven_five()}\n{eleven_six()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                                
                            elif eleven_one_test() == 't' and eleven_two_test() == 't' and eleven_three_test() == 't' and eleven_four_test() == 't' and eleven_five_test() == 't':
                                await bot.send_message(message.from_user.id, f"{eleven_one()}\n{eleven_two()}\n{eleven_three()}\n{eleven_four()}\n{eleven_five()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()

                            elif eleven_one_test() == 't' and eleven_two_test() == 't' and eleven_three_test() == 't' and eleven_four_test() == 't':
                                await bot.send_message(message.from_user.id, f"{eleven_one()}\n{eleven_two()}\n{eleven_three()}\n{eleven_four()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()

                            elif eleven_one_test() == 't' and eleven_two_test() == 't' and eleven_three_test() == 't':
                                await bot.send_message(message.from_user.id, f"{eleven_one()}\n{eleven_two()}\n{eleven_three()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                            
                            elif eleven_one_test() == 't' and eleven_two_test() == 't':
                                await bot.send_message(message.from_user.id, f"{eleven_one()}\n{eleven_two()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                            
                            elif eleven_one_test() == 't':
                                await bot.send_message(message.from_user.id, f"{eleven_one()}", reply_markup=keyboard11) 
                                await Schedule.choosing_school_day.set()
                        
                        else:
                            await bot.send_message(message.from_user.id, "Список замен пуст", reply_markup=keyboard11) 
                            await Schedule.choosing_school_day.set()

            else:
                await bot.send_message(message.from_user.id, "Список замен пуст", reply_markup=keyboard11) 
                await Schedule.choosing_school_day.set()

        case 'Помощь':
            await bot.send_message(message.from_user.id, "Для получения справки необходимо перейти в Меню Помощь.\n\n\
Для получения расписания необходимо перейти в Меню и Перезапустить меня!", reply_markup=types.ReplyKeyboardRemove())
            await state.finish()

@dp.message_handler(commands=['help'])    
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, "Сейчас ты находишься в Меню Помощь!\
        \n\nЕсли ты забрел сюда случайно, тогда открой Меню и Перезапусти меня)\
        \n\nhttp://poleski.luninec.edu.by - Много интересной информации здесь!")    

                
@dp.message_handler(commands=['admins_784'])
async def admins(message: types.Message, state: FSMContext):
    kb00 = [
        [types.KeyboardButton(text="Назад")]
    ]
    keyboard00 = types.ReplyKeyboardMarkup(keyboard=kb00, resize_keyboard=True)
    await bot.send_message(message.from_user.id, "Введите текст для рассылки", reply_markup=keyboard00)
    await Admin.text.set()

@dp.message_handler(
    state=Admin.text
)
async def text(message: types.Message, state: FSMContext):
    await state.update_data(text = message.text)
    user_data = await state.get_data()
    text1 = user_data['text']
    if text1 == 'Назад':
        await bot.send_message(message.from_user.id, "Рассылка отменена", reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
    
    else:
        sql.execute("SELECT user_id FROM users")
        ids = sql.fetchall()
        for num in ids:
            result = num[0]
            await bot.send_message(result, text1, reply_markup=types.ReplyKeyboardRemove())
        await state.finish()

     
if __name__ == '__main__':
    executor.start_polling(dp)
