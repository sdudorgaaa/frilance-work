from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import datetime
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=options)
options.add_argument("--disable-blink-features=AutomationControlled")
driver.get('https://1xstavka.ru/live/football')

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
}

time_range = []

for hour in range(0, 1):
    for minute in range(1, 60):
        time_range.append(f"{hour:02d}:{minute:02d}")


def generate_time_for_eleven():
    times = []
    hour, minute = 10, 0
    
    while hour < 12:
        time_str = f"{hour:02d}:{minute:02d}"
        times.append(time_str)
        minute += 1        
        if minute == 60:
            minute = 0
            hour += 1
    
    return times


filt_one = [] #Список для матчей прошедших первый этап фильтрации
filt_two = [] #Список для матчей прошедших второй этап фильтрации

def generate_numbers(start, end, precision):
    nums = []
    current = start
    while current <= end:
        nums.append(round(current, precision))
        current += 10**(-precision)
    return nums

def filt_one_two():
    g = driver.find_elements(By.CLASS_NAME, "dashboard-champ-content") #Ищем лиги в лайве 
    for num in g:  #Для каждой лиги из лайва
        try:
            h = num.find_element(By.CLASS_NAME, "c-events__time").text #Получаем время каждого матча в лиге
        except: 
            continue #Если не найдено - пропусккаем
        if h in time_range:   #Если время лежит в промежутке от 00:01 до 00:59
            y = num.find_element(By.CLASS_NAME, "c-events__liga") #Получаем название лиги
            print(f"Лига {y.text}")
            t = num.find_elements(By.CLASS_NAME, "c-events__name") #Получаем лигу для извлечения ссылки на матч
            for nam in t: #Для каждой лиги для ссылки
                url_rut = nam.get_attribute("href") #Получаем атрибут с ссылкой
            url_r = url_rut.split("/") #Делим строку для извлечения id
            lin = [] #Создаём список для id из ссылки
            for numb in url_r[6]: #Для части строки с id получаем id
                f = numb.isdigit()
                if f == True:
                    lin.append(numb)
            link_m = ''.join(lin) #Создаём строку с id
            id_mat = link_m[:9] #Убираем лишнее из строки с id (если оно есть)
            sleep(1.5)
            c = requests.get(f"https://1xstavka.ru/LiveFeed/GetGameZip?id={id_mat}&lng=ru&cfview=0&isSubGames=true&GroupEvents=true&allEventsGroupSubGames=true&countevents=250&partner=51&grMode=2&marketType=1&isNewBuilder=true", timeout=30, headers=headers).json() #Делаем get запрос по полученному id на сервер и приобразовываем его из json
            sleep(1.5)
            try:
                o = c["Value"]["GE"][0]["E"][0][0]["C"] #Получаем кэф на первую комманду
            except:
                continue #Если не неайден - пропускаем

            try:
                o1 = c["Value"]["GE"][0]["E"][2][0]["C"] #Получаем кэф на вторую комманду
            except:
                continue  #Если не неайден - пропускаем
            try:
                k = c["Value"]["GE"][3]["E"][0][0]["C"] # Получаем кэф на ТБ 1.5
            except:
                continue
        
            p = list(generate_numbers(1.1, 1.4, 3)) # Список подходящих кэфов на фаворита
            i = list(generate_numbers(1.1, 2.1, 3)) # Список подходящих кэфов на ТБ 1.5
            if url_rut in filt_two:
                continue

            if o < o1: # Если первая комманда фаворит
                if o in p: # Если кэф подходит
                    if k in i: # Если тотал подходит
                        print (f"1 kom {o}")
                        print (k)
                        print("Первый этап фильрации обновлён")
                        filt_one.append(url_rut) # Добавляем матч в список первого этапа фильтрации

            elif o1 < o: # Если вторая комманда фаворит
                if o1 in p: # Если кэф подходит
                    if k in i: # Если тотал подходит
                        print (f"2 kom {o1}")
                        print(k)
                        print("Первый этап фильрации обновлён")
                        filt_one.append(url_rut) # Добавляем матч в список первого этапа фильтрации
        else: 
            continue

            # Начинаем второй этап фильтрации

    for num2 in filt_one: # Для каждого матча(ссылка) из второго этапа фильтрации
        #print(f"Каждая ссылка из первого этапа {num2}")
        if h in generate_time_for_eleven(): # Проверяем на условие +- 11 минут, если подходит 
            jok = driver.find_elements(By.CLASS_NAME, "c-events-scoreboard.c-events-scoreboard--hor-view") # Ищем контейнеры со всемми матчами
            for num7 in jok: # Для каждого контейнера
                try:
                    nm = num7.find_element(By.CLASS_NAME, "c-events__name") # Получаем ссылку на матч 
                    mii = nm.get_attribute("href")
                except: 
                    continue
                #print (f"Полученная ссылка {mii}")
                if mii == num2: # Если полученная ссылка совпадает с ссылкой матча из списка фильтров 
                    ty = num7.find_elements(By.CLASS_NAME, "c-events-scoreboard__cell.c-events-scoreboard__cell--all") # Ищем счёт
                    hui = [] # Создаём список для счёта 
                    for numio in ty: # Для каждого значения (их всего два)
                        hui.append(numio.text) # Добавляем в список
                    if hui[0] == '0' and hui[1] == '0': # Проверяем счёт, если 0:0
                        print(hui)
                        filt_two.append(num2)
                        print("Второй этап фильтрации обновлён")
                    else:
                        filt_one.remove(num2) # Если счёт не 0:0 удаляем матч из нашего списка
                        print ("Матч удалён")
                        print(f"{num2} не прошёл второй этап фильрации")
                else:
                    continue
        else: 
            continue
    
    sleep(5)
    driver.refresh()
    return filt_two

def get_schet(link_for_schet): #Функция для получения счёта матчей уже отправленных ботом
        jok = driver.find_elements(By.CLASS_NAME, "c-events-scoreboard.c-events-scoreboard--hor-view") # Ищем контейнеры со всемми матчами
        for num7 in jok: # Для каждого контейнера
            try:
                nm = num7.find_element(By.CLASS_NAME, "c-events__name") # Получаем ссылку на матч 
                mii = nm.get_attribute("href")
            except: 
                continue
            if mii == link_for_schet:
                ty = num7.find_elements(By.CLASS_NAME, "c-events-scoreboard__cell.c-events-scoreboard__cell--all") # Ищем счёт
                hui_two = [] # Создаём список для счёта 
                for numio in ty: # Для каждого значения (их всего два)
                    hui_two.append(numio.text) # Добавляем в список
        try:
            return hui_two
        except:
            pass
            

def three_control(lam): #Функция для чека счета уже отправленных матчей и анализа нужно ли менять сообщение 
        for lam2 in lam[1]:
            jop = get_schet(lam2)

            if jop[0] == lam[2] and jop[1] == lam[3]:
                continue

            else:
                new = (jop[0] + jop[1]) - (lam[2] + lam[3]) 
                return  lam[1], lam[2], lam[3], new




