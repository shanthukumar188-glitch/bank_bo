import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="db",   # 👈 this is docker service name
        user="root",
        password="Shanthu@1234",
        database="bankdb"
    )
