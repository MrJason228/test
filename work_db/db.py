import sqlite3

connect = sqlite3.connect("shop.db")
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(70),
        price INTEGER,
        count INTEGER
    )
""")


# with open('work_db//script.sql', 'r', encoding='utf-8') as f:
#     cursor.executescript(f.read())

# product2 = ["MacBook Pro", 2354, 20]

product_list = [
    # ['Samsing Galaxy S90', 300, 100],
    # ['Lenovo R34', 200, 15]
]

cursor.executemany("INSERT INTO products(name, price, count) VALUES (?, ?, ?)", product_list)
connect.commit()


products = cursor.fetchall()
print(products)



cursor.execute("SELECT * FROM information")
# cursor.execute("SELECT * FROM products")
# cursor.execute("SELECT * FROM categories")

information = cursor.fetchall()
print(information)

cursor.close()
connect.close()