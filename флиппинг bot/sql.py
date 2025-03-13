import sqlite3 as sq
import time


def sq_write(link):
	with sq.connect(f"announcements.db") as con:
		cur = con.cursor()

		cur.execute("""CREATE TABLE IF NOT EXISTS announcements_history(
		link TEXT,
		time TEXT)""")

		cur.execute(f"""INSERT INTO announcements_history VALUES(?, ?)""", (link, time.time()))


def sq_check(link):
	with sq.connect(f"announcements.db") as con:
		cur = con.cursor()

		cur.execute("""CREATE TABLE IF NOT EXISTS announcements_history(
		link TEXT,
		time TEXT)""")

		a = cur.execute('SELECT * FROM announcements_history WHERE link=?', (link,)).fetchall()
		if a:
			return False
		else:
			sq_write(link)
			return True

