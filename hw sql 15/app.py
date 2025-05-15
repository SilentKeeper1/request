import sqlite3


conn = sqlite3.connect("company.db")
cursor = conn.cursor()


cursor.execute("DROP TABLE IF EXISTS employees")
cursor.execute("DROP TABLE IF EXISTS departments")


cursor.execute("""
CREATE TABLE departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES departments(id)
)
""")


cursor.execute("INSERT INTO departments (name) VALUES ('HR')")
cursor.execute("INSERT INTO departments (name) VALUES ('Finance')")


cursor.execute("INSERT INTO employees (name, department_id) VALUES ('Alice', (SELECT id FROM departments WHERE name = 'HR'))")
cursor.execute("INSERT INTO employees (name, department_id) VALUES ('Bob', (SELECT id FROM departments WHERE name = 'HR'))")
cursor.execute("INSERT INTO employees (name, department_id) VALUES ('Charlie', (SELECT id FROM departments WHERE name = 'Finance'))")


cursor.execute("""
UPDATE employees
SET department_id = (SELECT id FROM departments WHERE name = 'Finance')
WHERE department_id = (SELECT id FROM departments WHERE name = 'HR')
""")


cursor.execute("""
SELECT employees.name AS employee_name, departments.name AS department_name
FROM employees
JOIN departments ON employees.department_id = departments.id
""")


rows = cursor.fetchall()
print("Працівники після оновлення:")
for row in rows:
    print(f"{row[0]} → {row[1]}")


conn.commit()
conn.close()