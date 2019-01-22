import mysql.connector


class UseDatabase:
    """Инициализация конфиг файла"""
    def __init__(self, config: dict) -> None:
        self.configuration = config

    """Настройка подключение к базе"""
    def __enter__(self) -> 'cursor':
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor

    """Заверщающий код"""
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
