import sqlite3
from datetime import datetime

DB_NAME = 'waitlist.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS waitlist (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            source TEXT,
            timestamp TEXT NOT NULL,
            website TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_email(email, source, website):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        timestamp = datetime.now().isoformat()
        c.execute('INSERT INTO waitlist (email, source, timestamp, website) VALUES (?, ?, ?, ?)',
                  (email, source, timestamp, website))
        conn.commit()
        return {'success': True, 'isDuplicate': False}
    except sqlite3.IntegrityError:
        return {'success': True, 'isDuplicate': True}
    except Exception as e:
        return {'success': False, 'message': str(e)}
    finally:
        conn.close()

if __name__ == '__main__':
    init_db()
    print("Database initialized.")
