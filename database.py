import sqlite3

DB_NAME = 'repair_requests.db'


def get_connection():
    """Подключаемся к базе данных"""
    return sqlite3.connect(DB_NAME)


def create_tables():
    """Создаём таблицы, если их нет"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            equipment TEXT NOT NULL,
            problem TEXT NOT NULL,
            requester TEXT NOT NULL,
            status TEXT DEFAULT 'Новая',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()


def add_request(equipment, problem, requester):
    """Добавляем новую заявку в БД"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO requests (equipment, problem, requester)
        VALUES (?, ?, ?)
    ''', (equipment, problem, requester))

    conn.commit()
    conn.close()


def get_all_requests():
    """Получаем все заявки из БД"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM requests ORDER BY created_at DESC')
    requests = cursor.fetchall()

    conn.close()

    requests_list = []
    for req in requests:
        requests_list.append({
            'id': req[0],
            'equipment': req[1],
            'problem': req[2],
            'requester': req[3],
            'status': req[4],
            'created_at': req[5]
        })

    return requests_list


def update_status(request_id, new_status):
    """Обновляем статус заявки"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE requests SET status = ? WHERE id = ?
    ''', (new_status, request_id))

    conn.commit()
    conn.close()