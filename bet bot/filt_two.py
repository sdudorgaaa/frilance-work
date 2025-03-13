from parce import get_schet
from time import sleep
from parce import headers
import requests

def supec(nam): 
    url_r = nam.split("/") #Делим строку для извлечения id
    lin = [] #Создаём список для id из ссылки
    for numb in url_r[6]: #Для части строки с id получаем id
        f = numb.isdigit()
        if f == True:
            lin.append(numb)
    link_m = ''.join(lin) #Создаём строку с id
    id_mat = link_m[:9] #Убираем лишнее из строки с id (если оно есть)
    sleep(0.5)
    gou = requests.get(f"https://1xstavka.ru/LiveFeed/GetGameZip?id={id_mat}&lng=ru&cfview=0&isSubGames=true&GroupEvents=true&allEventsGroupSubGames=true&countevents=250&partner=51&grMode=2&marketType=1&isNewBuilder=true", timeout=30, headers=headers).json()
    yui = get_schet(nam)
    lig = gou["Value"]["L"]
    kom1 = gou["Value"]["O1"]
    kom2 = gou["Value"]["O2"]
    o = yui[0]
    o1 = yui[1]
    
    return lig, kom1, kom2, o ,o1


    

        