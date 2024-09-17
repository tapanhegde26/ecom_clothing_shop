from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv('MYSQL_HOST', 'localhost'),
        user=os.getenv('MYSQL_USER', 'root'),
        password=os.getenv('MYSQL_PASSWORD', 'password'),
        database=os.getenv('MYSQL_DB', 'ecommerce')
    )

# Fetch all products from the database
def fetch_products():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)  # Use dictionary=True to get column names in the result
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    cursor.close()
    connection.close()
    return products

@app.route('/products', methods=['GET'])
def get_products():
    products = fetch_products()
    return jsonify(products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

