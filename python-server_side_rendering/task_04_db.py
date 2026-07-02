#!/usr/bin/python3
"""Flask application displaying product data from JSON, CSV or SQLite."""
import csv
import json
import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)


def create_database():
    """Create products.db and populate it if it is empty."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute('SELECT COUNT(*) FROM Products')
    if cursor.fetchone()[0] == 0:
        cursor.executemany(
            'INSERT INTO Products (id, name, category, price) '
            'VALUES (?, ?, ?, ?)',
            [
                (1, 'Laptop', 'Electronics', 799.99),
                (2, 'Coffee Mug', 'Home Goods', 15.99),
            ]
        )
    conn.commit()
    conn.close()


def read_json_products():
    """Return the list of products stored in products.json."""
    with open('products.json') as json_file:
        return json.load(json_file)


def read_csv_products():
    """Return the list of products stored in products.csv."""
    products = []
    with open('products.csv', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price']),
            })
    return products


def read_sql_products():
    """Return the list of products stored in products.db."""
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]


@app.route('/products')
def products():
    """Display products from the requested source, optionally filtered."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ('json', 'csv', 'sql'):
        return render_template('product_display.html', error='Wrong source')

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template(
                'product_display.html', error='Product not found')

    try:
        if source == 'json':
            products_list = read_json_products()
        elif source == 'csv':
            products_list = read_csv_products()
        else:
            products_list = read_sql_products()
    except (FileNotFoundError, sqlite3.Error):
        return render_template('product_display.html', error='Wrong source')

    if product_id is not None:
        products_list = [
            product for product in products_list
            if product['id'] == product_id
        ]
        if not products_list:
            return render_template(
                'product_display.html', error='Product not found')

    return render_template('product_display.html', products=products_list)


if __name__ == '__main__':
    create_database()
    app.run(debug=True, port=5000)
