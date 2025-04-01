square_kitchen = None
height = None
windows = None
dangerous = None
heating = None


def analytics(price, price_cian, price_m2, creator, about, qw_all, link_for_ret, price_for_ret, img_prev, qw_all_for_ret):
	global square_kitchen, height, windows, heating, dangerous
	lvl = 0
	if price and price_cian:
		try:
			price_cian = price_cian[:-6]
			price_cian = float(price_cian.replace(',', '.')) * 1000000
			price = price[:-2]
			price = float(price.replace(' ', ''))
			ps = price_cian - price
			if ps > 500000:
				lvl += 40
			elif ps > 300000:
				lvl += 30
			elif ps > 100000:
				lvl += 20
			else:
				if abs(ps) < 100000:
					lvl += 10
		except:
			lvl += 18
	else:
		lvl += 18

	if price_m2:
		try:
			price_m2 = price_m2[16:-5]
			price_m2 = float(price_m2.replace(' ', ''))
			if price_m2 < 85000:
				lvl += 20
			elif price_m2 < 95000:
				lvl += 15
			elif price_m2 < 105000:
				lvl += 10
			else:
				lvl += 5
		except:
			lvl += 7
	else:
		lvl += 7

	if creator:
		if creator == 'Агенство' or creator == 'Риелтор':
			lvl += 15
		elif creator == 'Собственник':
			lvl += 20
		elif creator == 'Застройщик':
			lvl += 10
	else:
		lvl += 15

	if about:
		about = about.split('\n')
		for i, v in enumerate(about):
			if v == 'Площадь кухни':
				try:
					square_kitchen = int(about[i + 1])
				except:
					square_kitchen = 7
			elif v == 'Высота потолков':
				try:
					height = about[i + 1]
					height = height.replace(',', '.')
					height = float(height[:-2])
				except:
					height = 10
			elif v == 'Вид из окон':
				try:
					windows = about[i + 1]
				except:
					windows = 'На улицу'
			elif v == 'Аварийность':
				try:
					dangerous = about[i + 1]
				except:
					dangerous = 'Нет'
			elif v == 'Отопление':
				try:
					heating = about[i + 1]
				except:
					height = "другое"

	if square_kitchen:
		if square_kitchen > 8:
			lvl += 20
		elif square_kitchen > 6:
			lvl += 10
		else:
			lvl += 5
	else:
		lvl += 10

	if height:
		if height > 3:
			lvl += 20
		elif height > 2.7:
			lvl += 15
		elif height > 2.5:
			lvl += 10
		else:
			lvl += 5
	else:
		lvl += 10

	if windows:
		if windows != 'На улицу':
			lvl += 20
		else:
			lvl += 10
	else:
		lvl += 10

	if heating:
		if heating == 'Центральное':
			lvl += 20
		else:
			lvl += 10
	else:
		lvl += 10

	if dangerous:
		if dangerous == 'Нет':
			lvl += 20
	else:
		lvl += 10

	r = len(price_for_ret)
	if r == 0:
		a = 10000000
	else:
		a = (sum(price_for_ret) / len(price_for_ret)) * 1000000

	c = a - price

	

	print(price, price_cian, price_m2, creator, dangerous, height, heating, square_kitchen, windows, qw_all, link_for_ret, price_for_ret, img_prev, qw_all_for_ret, c)
	return lvl, price_cian, price_m2, creator, dangerous, height, heating, square_kitchen, windows, qw_all, link_for_ret, price_for_ret, img_prev, price, qw_all_for_ret, c

