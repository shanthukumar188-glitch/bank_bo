import mysql.connector
import time

def get_connection():
    while True:
        try:
            conn = mysql.connector.connect(
                host="db",
                user="root",
                password="Shanthu@123",
                database="bankdb"
            )
            return conn
        except:
            print("⏳ Waiting for MySQL...")
            time.sleep(3)
