from flask import Flask, render_template, request, jsonify
from db import get_connection
import time

app = Flask(__name__)

def init_db():
    while True:
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS customers (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100),
                    balance FLOAT
                )
            """)

            conn.commit()
            conn.close()
            print("✅ Database initialized")
            break

        except Exception as e:
            print("⏳ Waiting for DB...", e)
            time.sleep(3)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add', methods=['POST'])
def add_customer():
    data = request.get_json()
    name = data['name']
    balance = data['balance']

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO customers (name, balance) VALUES (%s, %s)",
        (name, balance)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Customer added"})


@app.route('/customers')
def get_customers():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM customers")
    data = cursor.fetchall()

    conn.close()

    return jsonify(data)


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
