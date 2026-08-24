from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
import os


app = Flask(__name__)

CORS(app)


# Database connection
def get_db_connection():

    connection = mysql.connector.connect(

        host=os.getenv("DB_HOST", "localhost"),

        user=os.getenv("DB_USER", "shopflow"),

        password=os.getenv("DB_PASSWORD", "shopflowpassword"),

        database=os.getenv("DB_NAME", "shopflow")

    )

    return connection


# Health check
@app.route("/health")
def health():

    return jsonify({
        "status": "UP",
        "application": "ShopFlow"
    })


# Get all products
@app.route("/api/products", methods=["GET"])
def get_products():

    connection = get_db_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM products"
    )

    products = cursor.fetchall()

    cursor.close()

    connection.close()

    return jsonify(products)


# Get single product
@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product(product_id):

    connection = get_db_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM products WHERE id = %s",
        (product_id,)
    )

    product = cursor.fetchone()

    cursor.close()

    connection.close()


    if product:

        return jsonify(product)

    return jsonify({
        "error": "Product not found"
    }), 404


# Create product
@app.route("/api/products", methods=["POST"])
def create_product():

    from flask import request

    data = request.json

    name = data["name"]

    description = data["description"]

    price = data["price"]


    connection = get_db_connection()

    cursor = connection.cursor()

    cursor.execute(

        """
        INSERT INTO products
        (name, description, price)

        VALUES (%s, %s, %s)
        """,

        (name, description, price)

    )

    connection.commit()

    product_id = cursor.lastrowid

    cursor.close()

    connection.close()


    return jsonify({

        "message": "Product created",

        "product_id": product_id

    }), 201


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
