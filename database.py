import sqlite3
import logging

DATABASE_PATH = 'booking.db'

def get_db_connection(db_path=DATABASE_PATH):
    """Establishes a connection to the database."""
    try:
        return sqlite3.connect(db_path)
    except Exception as e:
        logging.error(f'Error connecting to database: {e}')
        return None

def init_db(db_path=DATABASE_PATH):
    """Initializes the database and creates tables if they don't exist."""
    try:
        with get_db_connection(db_path) as conn:
            c = conn.cursor()
            c.execute("""
                CREATE TABLE IF NOT EXISTS Services (
                    id INTEGER PRIMARY KEY, name TEXT NOT NULL, duration INTEGER NOT NULL
                )
            """)
            c.execute("""
                CREATE TABLE IF NOT EXISTS Reservations (
                    id INTEGER PRIMARY KEY, client_name TEXT NOT NULL, client_phone TEXT NOT NULL,
                    service_id INTEGER NOT NULL, slot TEXT NOT NULL,
                    FOREIGN KEY (service_id) REFERENCES Services(id)
                )
            """)
            c.execute('SELECT COUNT(*) FROM Services')
            if c.fetchone()[0] == 0:
                logging.info('Populating Services table with sample data.')
                sample_services = [
                    ("Men's Cut", 30), ("Women's Cut", 60), ('Color & Style', 120)
                ]
                c.executemany('INSERT INTO Services (name, duration) VALUES (?, ?)', sample_services)
            conn.commit()
            logging.info('Database initialized successfully.')
    except Exception as e:
        logging.error(f'Error initializing database: {e}')

def get_services(db_path=DATABASE_PATH):
    """Fetches all services from the database."""
    try:
        with get_db_connection(db_path) as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM Services')
            return c.fetchall()
    except Exception as e:
        logging.error(f'Error fetching services: {e}')
        return []

def create_booking(client_name, client_phone, service_id, slot, db_path=DATABASE_PATH):
    """Creates a new booking in the database."""
    try:
        with get_db_connection(db_path) as conn:
            c = conn.cursor()
            c.execute(
                'INSERT INTO Reservations (client_name, client_phone, service_id, slot) VALUES (?, ?, ?, ?)',
                (client_name, client_phone, service_id, slot),
            )
            conn.commit()
            logging.info(f'New booking created for {client_name} at {slot}.')
            return True
    except Exception as e:
        logging.error(f'Error creating booking for {client_name}: {e}')
        return False
