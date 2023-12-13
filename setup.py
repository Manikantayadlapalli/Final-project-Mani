import sqlite3

conn = sqlite3.connect('vehicle_companion.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS vehicles')
cursor.execute('DROP TABLE IF EXISTS companions')

cursor.execute('''
CREATE TABLE IF NOT EXISTS companions (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS vehicles (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 title TEXT NOT NULL,
 release_year INTEGER,
 companion_id INTEGER,
 FOREIGN KEY (companion_id) REFERENCES companions(id)
)
''')

cursor.execute("INSERT INTO companions (name) VALUES ('Benz')")
cursor.execute("INSERT INTO companions (name) VALUES ('Audi')")
cursor.execute("INSERT INTO companions (name) VALUES ('Toyota')")
cursor.execute("INSERT INTO companions (name) VALUES ('Honda')")
cursor.execute("INSERT INTO companions (name) VALUES ('Ford')")
cursor.execute("INSERT INTO companions (name) VALUES ('Tesla')")
cursor.execute("INSERT INTO vehicles (title, release_year, companion_id) VALUES ('Benz Model A', 2019, 1)")
cursor.execute("INSERT INTO vehicles (title, release_year, companion_id) VALUES ('Audi Model B', 2020, 2)")

conn.commit()
