import sqlite3

connection = sqlite3.connect("../contacts.db")

create_contacts_table_query = """
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    favorite INTEGER DEFAULT 0
);
"""
insert_contacts_query = """
INSERT INTO contacts (name, age, favorite)
VALUES ('Олексій', 30, 1),
       ('Марія', 22, 0),
       ('Іван', 27, 1),
       ('Андрій', 24, 0);
"""
connection.execute(create_contacts_table_query)
connection.execute(insert_contacts_query)
connection.commit()

connection = sqlite3.connect("../contacts.db")

for d in connection.execute("SELECT * FROM contacts WHERE age > 25;"):
    print(d)

print("+" * 40)
print()

for d in connection.execute("SELECT * FROM contacts WHERE favorite = 1;"):
    print(d)

connection.close()