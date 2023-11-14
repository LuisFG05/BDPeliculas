import sqlite3

conn = sqlite3.connect('BDPeliculas')
cursor = conn.cursor()
cursor.execute(''' CREATE TABLE IF NOT EXISTS pelicula(
    id INTEGER PRIMARY KEY, titulo TEXT NOT NULL, director TEXT,
    lanzamiento INTERGER
)''')


cursor.execute('INSERT INTO pelicula(titulo, director, lanzamiento) VALUES(?,?,?)',('LOS SIMPSON LA PELICULA', 'David Silverman', 2007))
conn.commit()

cursor.execute('SELECT *FROM pelicula')
pelicula = cursor.fetchall()

print('lista de peliculas: ')
for peliculas in pelicula:
    print(peliculas)
    
conn.close()