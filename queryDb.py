import sqlite3

conn = sqlite3.connect("/home/shad/Desktop/shad/Anki/User 1/collection.anki2")
conn.row_factory= sqlite3.Row
c = conn.cursor()
print c.execute("SELECT notes.* FROM cards inner join notes on cards.nid = notes.id")


for row in c.fetchall():
    print row['flds']

