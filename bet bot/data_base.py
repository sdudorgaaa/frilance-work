import sqlite3

conn = sqlite3.connect('orders.db')

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS filt_three(
   mes_id INT ,
   href TEXT,
   count INT,
   count1 INT);
""")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS lig_delete(
   lig_name TEXT);
""")
conn.commit()

def add_filt_three(id_three, link, o, o1):  #Функция для заполнения таблицы данными для третьего этапа фильтрации
    for_add = (id_three, link, o, o1)
    cur.execute("INSERT INTO filt_three VALUES(?, ?, ?, ?);", for_add)
    conn.commit()

def get_three(): #Функция для получения всего содержимого таблицы
    cur.execute("SELECT * FROM filt_three;")
    all_results = cur.fetchall()
    return all_results

def grom(lig):
    for_add = (lig)
    cur.execute("INSERT INTO lig_delete VALUES(?);", for_add)
    conn.commit()

def get_block_list(): #Функция для получения всего содержимого таблицы
    cur.execute("SELECT * FROM lig_delete;")
    all_results = cur.fetchall()
    return all_results
