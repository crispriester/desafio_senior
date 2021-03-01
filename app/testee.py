import sqlite3

conexao = sqlite3.connect("evento.db")
cursor = conexao.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS tab1 (id integer, nome text)")
cursor.execute("INSERT INTO tab1 VALUES (?, ?)", (1, "a",))
cursor.execute("INSERT INTO tab1 VALUES (?, ?)", (2, "b",))
cursor.execute("INSERT INTO tab1 VALUES (?, ?)", (3, "c",))


cursor.execute("CREATE TABLE IF NOT EXISTS tab2 (id integer, id_tab1 integer)")
cursor.execute("INSERT INTO tab2 VALUES (?, ?)", (1, 1))
cursor.execute("INSERT INTO tab2 VALUES (?, ?)", (2, 3))

cursor.execute("SELECT tab1.id, tab2.id_tab1 FROM tab1 INNER JOIN tab2 ON tab1.id = tab2.id_tab1")

a = cursor.fetchall()

for x in a:
  print(x)
