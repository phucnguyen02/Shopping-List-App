import sqlite3

conn = sqlite3.connect('shopping_lists.db')

#conn = sqlite3.connect(":memory:")
c = conn.cursor()

# c.execute("DROP TABLE if exists shopping_lists")
# c.execute("""CREATE TABLE shopping_lists (
#        id INTEGER PRIMARY KEY AUTOINCREMENT,
#        name text
#        )""")

# c.execute("DROP TABLE if exists shopping_items")
# c.execute("""CREATE TABLE shopping_items (
#        item_id INTEGER PRIMARY KEY AUTOINCREMENT,
#        list_id INTEGER,
#        name text
#        )""")

conn.commit()
conn.close()
