import sqlite3

conn = sqlite3.connect("customer.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Customers (
    CustomerID INTEGER PRIMARY KEY,
    CustomerName TEXT,
    ContactName TEXT,
    Address TEXT,
    City TEXT,
    PostalCode TEXT,
    Country TEXT
)
""")
customers_data = [
    (89, 'White Clover Markets', 'Karl Jablonski', '305 - 14th Ave. S. Suite 3B', 'Seattle', '98128', 'USA'),
    (90, 'Wilman Kala', 'Matti Karttunen', 'Keskuskatu 45', 'Helsinki', '21240', 'Finland'),
    (91, 'Wolski', 'Zbyszek', 'ul. Filtrowa 68', 'Walla', '01-012', 'Poland')
]

cursor.executemany("INSERT INTO Customers VALUES (?, ?, ?, ?, ?, ?, ?)", customers_data)
conn.commit()
cursor.execute("SELECT * FROM Customers")
rows = cursor.fetchall()

for row in rows:
    print(row)
conn.close()
