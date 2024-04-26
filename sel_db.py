import requests
import sqlite3
from datetime import date, time

TOKEN = ""
chat_id = ""

today = str(date.today())
#print(today)
# Устанавливаем соединение с базой данных
connection = sqlite3.connect('instance/diary.db')
cursor = connection.cursor()
records = []

# Выбираем нужный столбец
cursor.execute('SELECT CAST(subtitle AS TEXT) FROM card')

rows = cursor.fetchall()

#today="2024-04-27"

# while rows is not None:
#     print(rows[0])
#     rows = cursor.fetchone()
# #time.sleep(60)
#цикл проверки где сравниваем значение в базе с текущей датой. если есть совпадение отправляем сообщение в телеграм
for row in rows:
   print(row)
   if (row[0] == today):
      message = "На текущую дату: "
      message1 = " у вас есть заметка"
      url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}{today}{message1}"
      print(requests.get(url).json())  # Эта строка отсылает сообщение
      #print ("попал")
   else:
      print("")

#   print(row[0] == today)
# Закрываем соединение
connection.close()
