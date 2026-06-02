import os
import sqlite3

def init_salon_db():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "salon.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_key = ON")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS masters(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        specialty TEXT NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS services(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        price REAL NOT NULL,
        duration_min INTEGER NOT NULL,
        master_id INTEGER,
        FOREIGN KEY (master_id) REFERENCES master(id) ON DELETE SET NULL
    );
    """)

    cursor.execute("DELETE FROM services;")
    cursor.execute("DELETE FROM masters;")

    cursor.execute("INSERT INTO masters (name, specialty) VALUES ('Алла Петровна', 'Топ стилист'), ('Игорь','Барбер'), ('Елена','Косметолог');")

    test_services = [
        ("Женская стрижка", 2500.0, 60, 1),
        ("Окрашивание волос", 3000.0, 90, 1),
        ("Мужская стрижка + укладка бороды", 1500.0, 60, 2),
        ("Детская стрижка", 900.0, 30, 2),
        ("Чистка лица ультра звуком", 800.0, 50, 3),
    ]

    cursor.executemany("INSERT INTO services (title, price, duration_min, master_id) VALUES (?, ?, ?, ?);",
                   test_services,
    )

    conn.commit()
    conn.close()
    print("БД создана")


if __name__ == "__main__":
    init_salon_db()