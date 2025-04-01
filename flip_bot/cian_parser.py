import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium_stealth import stealth
import analytics
import main
from time import sleep



options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)
options.add_argument("--disable-blink-features=AutomationControlled")


stealth(driver,
        languages=["en-US", "ru"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

delay = 5

def get_links():
	lst = []
	fl = True
	i1 = 1
	driver.get(main.link1.format(i1))
	while fl:
		delay2 = 7
		sleep(delay2)
		for i in range(0, 190):
			driver.execute_script("window.scrollTo(1000, " + str(i * 70) + ");")
			time.sleep(0.02)
		block = driver.find_element(By.CLASS_NAME, '_93444fe79c--wrapper--W0WqH')
		sales = block.find_elements(By.CLASS_NAME, '_93444fe79c--media--9P6wN')

		for i in sales:
			lst.append(i.get_attribute('href'))
		try:
			if i1 >= main.len1:
				break

			i1 += 1
			driver.get(main.link1.format(i1))
		except:
			break
	return len(lst), lst


def get_element(variable, value):
	if not variable:
		try:
			return driver.find_element(By.CLASS_NAME, value).text
		except:
			pass
	return variable


def get_info(link):
	driver.get(link)
	driver.execute_script("window.scrollBy(1000, 0)")
	time.sleep(1)

	price = None
	price_m2 = None
	about = None
	price_cian = None
	hwo1 = None
	hwo2 = None
	hwo3 = None
	hwo4 = None

	for i in range(0, 70):
		time.sleep(0.02)
		price = get_element(price, 'a10a3f92e9--amount--ON6i1')
		price_m2 = get_element(price_m2, 'a10a3f92e9--item--iWTsg')
		about = get_element(about, 'a10a3f92e9--section--eHvYg')
		price_cian = get_element(price_cian, 'a10a3f92e9--price--w7ha0')
		try:
			qw_all = driver.find_element(By.CLASS_NAME, 'a10a3f92e9--info-value--bm3DC').text
		except:
			qw_all = driver.find_element(By.CLASS_NAME, 'a10a3f92e9--color_black_100--kPHhJ.a10a3f92e9--lineHeight_6u--A1GMI.a10a3f92e9--fontWeight_bold--ePDnv.a10a3f92e9--fontSize_16px--RB9YW.a10a3f92e9--display_block--pDAEx.a10a3f92e9--text--g9xAG').text
		hwo1 = get_element(hwo1, 'a10a3f92e9--main--_w7i2')     # Агенство
		hwo2 = get_element(hwo1, 'a10a3f92e9--wrapper--vspMS')  # Риелтор
		hwo3 = get_element(hwo1, 'a10a3f92e9--wrapper--tnKaw')  # собственник
		hwo4 = get_element(hwo1, 'a10a3f92e9--logo--QGiT1')  # застройщик
		prev = driver.find_element(By.CLASS_NAME, 'a10a3f92e9--container--KIwW4.a10a3f92e9--container--contain--cYP76')
		img_prev = prev.get_attribute('src')
		


		driver.execute_script("window.scrollBy(0, 3200)")

		sleep(delay)
	
		share = driver.find_element(By.CLASS_NAME,  'a10a3f92e9--show-more-btn--wmYm5')
		driver.execute_script("arguments[0].click();",share)

		sleep(delay)

		link_now = driver.current_url
		link_now_id = []
		for num in link_now:
			f = num.isdigit()
			if f == True:
				link_now_id.append(num)
		link_now_id_str = ''.join(link_now_id) #Ссылка на котрой мы сейчас находимся в цифрах

		
		resp_post = driver.execute_script("const response = await fetch('https://api.cian.ru/valuation-offer-history/v4/get-house-offer-history-desktop/',{method: 'POST', body :JSON.stringify({'offerId':%s,'resultsOnPage':10,'page':1,'dealType':'sale','offerStatus':'published','isNearby':false}), headers: {'Content-Type': 'application/json'}}); return await response.json();" % (link_now_id_str)) #POST запрос на получение первых 10 конкурентов
		nums_two = resp_post["totalCount"]
		if nums_two <= 10:
			nums = list(range(nums_two))
		else:
			nums = [0,1,2,3,4,5,6,7,8,9]
		total_count = [] #Список в котором храняться первые 10 ссылок на конкурентов
		for num in nums:
			f = resp_post["offers"][num]["link"]
			total_count.append(f)
		
		concur_only = resp_post["totalCount"] - 10 # Кол-во конкурентов за исключением уже полученных
		conc_num = int(concur_only / 10) #Узнаем сколько запросов понадобиться отправить
		concur_num_lst = list(range(1, conc_num + 1)) #Создаём список с кол-вом требуемых запросов

		resp_post_lst = [] #Список со всеми ссылками на конкурентов кроме первых 10
		for num in concur_num_lst:
			sleep(delay)
			lun = driver.execute_script("const response = await fetch('https://api.cian.ru/valuation-offer-history/v4/get-house-offer-history-desktop/',{method: 'POST', body :JSON.stringify({'offerId':%s,'resultsOnPage':10,'page':%s,'dealType':'sale','offerStatus':'published','isNearby':false}), headers: {'Content-Type': 'application/json'}}); return await response.json();" % (link_now_id_str, 1 + num)) #Отправляе  запросы на оставшиеся квартиры конкурентов
			for numd in nums:
				f = lun["offers"][numd]["link"] #Ищем ссылки на конкурентов
				resp_post_lst.append(f) #Добавляем ссылки на конкурентов в список
		concur_link_all = resp_post_lst + total_count #Список со всеми ссылками на конкурентов
		print (concur_link_all)

		sleep(delay)
		link_for_ret = [] #Создаём список для ссылок
		price_for_ret = [] #Создаём список для цен
		qw_all_for_ret = [] #Создаём список для квадратуры конкурентов
		for num in concur_link_all:
			link_code = []
			lk = num
			for num_one in lk:
				f = num_one.isdigit()
				if f == True:
					link_code.append(num_one)
			my_string = ''.join(link_code)
			link_data = f'https://api.cian.ru/valuation-offer-history/v2/get-offer-from-history-web/?cianId={my_string}' #Собираем инфу о конкурентах
			driver.get(link_data)
		
			b = driver.find_element(By.XPATH,"//pre").text
			brah = eval(b)
			t = brah["features"]
			
			for num in t:   # Получаем нужную инфу о конкурентах
				arm = num["value"]
				if arm == "Евроремонт" or arm == "Дизайнерский":
					#print (arm)
					print (brah["title"][0:4])
					if float(qw_all[0:2]) - 10 >= float(brah["title"][0:4]) >= float(qw_all[0:2]) + 10:

						link_for_ret.append(brah["link"])
						#print(brah["link"])

						price_for_ret.append(brah["prices"]["price"][0:3])
						#print(brah["prices"]["price"])

						qw_all_for_ret.append(brah["title"][0:4])

		print(link_for_ret)
		print(price_for_ret)
		print(qw_all_for_ret)
		

		sleep(delay)
		driver.execute_script("window.history.go(-1)")
		sleep(delay)
		driver.execute_script("window.scrollTo(1000, 10000);")
		sleep(delay)
		
		
		creator = None
		if hwo1 is not None:
			creator = 'Агенство'
		elif hwo2 is not None:
			creator = 'Риелтор'
		elif hwo3 is not None:
			creator = 'Собственник'
		elif hwo4 is not None:
			creator = 'Застройщик'
		return price, price_cian, price_m2, creator, about, qw_all, link_for_ret, price_for_ret, img_prev, qw_all_for_ret
	
			


def get(link):
	c = 0
	a = get_info(link)
	for i in range(3):
		for j in a:
			if j is None:
				c += 1
		if c >= 2:
			time.sleep(10)
			a = get_info(link)
		else:
			break

	return analytics.analytics(*a)
