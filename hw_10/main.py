import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.executescript("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    birth_date TEXT NOT NULL,
    class_id INTEGER NOT NULL,
    phone_number TEXT UNIQUE,
    FOREIGN KEY (class_id) REFERENCES classes(id)
);

CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone_number TEXT UNIQUE,
    email TEXT UNIQUE,
    subject_id INTEGER,
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
);

CREATE TABLE IF NOT EXISTS classes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_name TEXT UNIQUE NOT NULL,
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
);

CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    subject_id INTEGER NOT NULL,
    teacher_id INTEGER NOT NULL,
    grade INTEGER CHECK (grade BETWEEN 1 AND 12),
    date TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (subject_id) REFERENCES subjects(id),
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
);

CREATE TABLE IF NOT EXISTS schedule (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_id INTEGER NOT NULL,
    subject_id INTEGER NOT NULL,
    teacher_id INTEGER NOT NULL,
    lesson_time TEXT NOT NULL,
    weekday TEXT CHECK (weekday IN ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')),
    FOREIGN KEY (class_id) REFERENCES classes(id),
    FOREIGN KEY (subject_id) REFERENCES subjects(id),
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
);
""")

cursor.executescript("""
INSERT OR IGNORE INTO subjects (id, subject_name) VALUES
(1, 'Mathematics'),
(2, 'Physics'),
(3, 'Literature');

INSERT OR IGNORE INTO teachers (id, first_name, last_name, phone_number, email, subject_id) VALUES
(1, 'Ivan', 'Petrov', '123456789', 'ivan.petrov@email.com', 1),
(2, 'Anna', 'Shevchenko', '987654321', 'anna.shevchenko@email.com', 2);

INSERT OR IGNORE INTO classes (id, class_name, teacher_id) VALUES
(1, '10-A', 1),
(2, '11-B', 2);

INSERT OR IGNORE INTO students (id, first_name, last_name, birth_date, class_id, phone_number) VALUES
(1, 'Dmytro', 'Ivanov', '2008-05-12', 1, '111222333'),
(2, 'Oksana', 'Kovalenko', '2007-09-23', 2, '444555666');

INSERT OR IGNORE INTO grades (student_id, subject_id, teacher_id, grade) VALUES
(1, 1, 1, 10),
(2, 2, 2, 8);

INSERT OR IGNORE INTO schedule (class_id, subject_id, teacher_id, lesson_time, weekday) VALUES
(1, 1, 1, '08:00', 'Monday'),
(2, 2, 2, '09:00', 'Tuesday');
""")

conn.commit()

tables = ["students", "teachers", "classes", "subjects", "grades", "schedule"]
for table in tables:
    print(f"\n{table.upper()}:")
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

cursor.close()
conn.close()

print("\nБаза даних заповнена та успішно виведена!")
