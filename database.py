import os
import mysql.connector


class Database:

    def __init__(self):
        db_config = {
            "host": os.getenv("DB_HOST", "localhost"),
            "user": os.getenv("DB_USER", "root"),
            "password": os.getenv("DB_PASSWORD", "Mkhatjwa10$"),
            "database": os.getenv("DB_NAME", "minipos"),
        }

        self.db = mysql.connector.connect(**db_config)
        self.cursor = self.db.cursor()

    def insert_sale(self, product):
        sql = """
        INSERT INTO sales (product_name, quantity, total)
        VALUES (%s,%s,%s)
        """

        values = (
            product.name,
            product.quantity,
            product.get_total(),
        )

        self.cursor.execute(sql, values)
        self.db.commit()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.db:
            self.db.close()
