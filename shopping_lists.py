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


# insert_list(list1)
# insert_list(list2)
#rename_list(list1, "Shopping List 3")
# c.execute("INSERT INTO shopping_lists (name) VALUES('Shopping List 1')")
# conn.commit()
# c.execute("INSERT INTO shopping_lists (name) VALUES('Shopping List 2')")
# conn.commit()

conn.commit()
conn.close()
