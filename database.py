import mysql.connector

class Database:

    def __init__(self):

        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mkhatjwa10$",
            database="minipos"
        )

        self.cursor = self.db.cursor()

    def insert_sale(self, product):

        sql = """
        INSERT INTO sales (product_name, quantity, total)
        VALUES (%s,%s,%s)
        """

        values = (
            product.name,
            product.quantity,
            product.get_total()
        )

        self.cursor.execute(sql, values)

        self.db.commit()