import sqlite3

connection = sqlite3.connect("contacts.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INT PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    email VARCHAR(30),
    phone VARCHAR(30),
    favorite BOOLEAN DEFAULT FALSE,
    user_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    age INT
);
""")

cursor.execute("INSERT INTO contacts (id, name, email, phone, favorite, user_id, age) VALUES (1, 'Ivan', 'ivan@gmail.com', '123-456', 1, 1, 30);")
cursor.execute("INSERT INTO contacts (id, name, email, phone, favorite, user_id, age) VALUES (2, 'Oleh', 'oleh@gmail.com', '987-654', 0, 2, 20);")
cursor.execute("INSERT INTO contacts (id, name, email, phone, favorite, user_id, age) VALUES (3, 'Anna', 'anna@gmail.com', '555-555', 1, 3, 27);")

connection.commit()

cursor.execute("""
SELECT * 
FROM contacts
WHERE age > 25;
""")

result = cursor.fetchall()
for row in result:
    print(row)

connection.close()
