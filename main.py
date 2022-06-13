import sqlite3

con = sqlite3.connect('hh.sqlite') # подключаемся к базе данных
cursor = con.cursor() # создаем курсор

cursor.execute('SELECT id, name FROM vacancy')  # выполняем запрос
result = cursor.fetchall() # запоминаем результат запроса в переменной result
print(result)

cursor.execute('SELECT v.name, r.name AS region_name FROM vacancy v, region r WHERE v.region_id == r.id')
result = cursor.fetchall() # запоминаем результат запроса в переменной result
print(result)

con.commit()
con.close() # закрываем подключение к базе данных