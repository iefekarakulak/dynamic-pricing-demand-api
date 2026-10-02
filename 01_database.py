import sqlite3

DB_NAME = "store.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            base_cost REAL NOT NULL
        )
    """)
    
    cursor.execute("SELECT COUNT(*) FROM products")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO products (name, base_cost) VALUES (?, ?)", ("Bluetooth Kulaklık", 100.0))
    
    conn.commit()
    conn.close()

def get_product(product_id: int):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, base_cost FROM products WHERE id = ?", (product_id,))
    product = cursor.fetchone()
    conn.close()
    return product

def add_product(name: str, base_cost: float):
    """Yeni ürün ekler."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, base_cost) VALUES (?, ?)", (name, base_cost))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id
