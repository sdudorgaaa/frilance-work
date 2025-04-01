import time
from aiogram import Bot, Dispatcher, executor, types
import cian_parser as cp
from sql import sq_check


bt = Bot("5738161405:AAGrLEPSLoxlVX42kftCfS3h3ioaHj7Jow4")  # Api токен бота
link1 = "https://tyumen.cian.ru/cat.php?deal_type=sale&engine_version=2&object_type%5B0%5D=1&offer_type=flat&p={}&region=5024&repair%5B0%5D=1&room2=1&sort=creation_date_asc"  # ссылка на список квартир где надо написать p={}
time1 = 3600    # Время в секундах определяющее частоту парсинга
len1 = 2   # число объявлений с указанными фильтрами деленое на 28 и округленное в большую сторону не меньше 2
lvl1 = 100   # оценка объявлений выше которой будут приходить в тг

dp = Dispatcher(bt)


@dp.message_handler(commands='start')
async def main(message: types.Message):
	while True:
		x = []
		count, lst = cp.get_links()
		for i in lst:
			if sq_check(i):
				score = cp.get(i)   
				if score[15] > 200000:
					list_conc =[]
					for num in score[10]:
						f = f"https://tymen.cian.ru{num}, "
						list_conc.append(f)
					list_conc_fin = ' '.join(list_conc)
					await bt.send_photo(message.from_user.id, photo=score[12], caption=f"🔸 Стоимость: {score[13]}\n\n🔹 Ссылка: {i}\n\n🔸 Владелец: {score[3]}\n\n🔹 Общая площадь: {score[9]}\n\n🔸 Ссылки на конкурентов: {list_conc_fin}")
		time.sleep(time1)    # Раз в какое время бот будет искать новые квартиры в секундах


if __name__ == "__main__":
	executor.start_polling(dp)
