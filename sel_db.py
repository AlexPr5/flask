import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('instance/diary.db')
cursor = connection.cursor()

# Выбираем всех пользователей

cursor.execute('SELECT CAST(subtitle AS TEXT) FROM card')

#cursor.execute('SELECT subtitle FROM card WHERE strftime('%Y-%m-%d %H:%M:%S', date_column)')
#cursor.execute('SELECT subtitle FROM card WHERE DATE(subtitle) = "ГГГГ-ММ-ДД"')
users = cursor.fetchall()

test = ('fddfdf')
test1 = ('fddfdf')
# Выводим результаты
for user in users:          
   #print(user == test)
   print(user)

    # if message.from_user.id not in user: # вот так не работает, работает только если писать result[0] и т.д.
    #     print("Выдает не зареган... Даже, если этот id есть в бд")
    # else:
    #     print("Вы уже зареганы в бд")
print (('test') == user)            #Тест равен пользователю
print (('test'))                    #Вывести "Тест"


# Закрываем соединение
connection.close()
