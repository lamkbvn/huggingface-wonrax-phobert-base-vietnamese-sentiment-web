import sqlite3
from config import Config

def get_db_connection():
    """Tạo kết nối database"""
    conn = sqlite3.connect(Config.DATABASE)
    conn.row_factory = sqlite3.Row
    return conn



def init_db():
    """Khởi tạo database và bảng"""
    conn = sqlite3.connect(Config.DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            sentiment TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()

def get_all_history():
    """Lấy tất cả lịch sử"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM history ORDER BY created_at DESC')
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_history_by_id(history_id):
    """Lấy một mục theo ID"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM history WHERE id = ?', (history_id,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def add_history( content ,  sentiment):
    """Thêm mục mới"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO history ( content ,  sentiment) '
                                    'VALUES ( ? , ?)',( content , sentiment))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id

def delete_history(history_id):
    """Xóa một mục"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM history WHERE id = ?', (history_id,))
    conn.commit()
    conn.close()

def clear_all_history():
    """Xóa tất cả lịch sử"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM history')
    conn.commit()
    conn.close()