import mysql.connector


class Config:
    def mySqlConnect():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="shop_product"
        )

    # def upload():
