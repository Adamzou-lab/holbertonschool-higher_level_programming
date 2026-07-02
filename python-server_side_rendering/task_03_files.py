#!/usr/bin/python3
"""Flask application displaying product data from JSON or CSV files."""
import csv
import json

from flask import Flask, render_template, request

app = Flask(__name__)


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


@app.route('/products')
def products():
    """Display products from the requested source, optionally filtered."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ('json', 'csv'):
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
        else:
            products_list = read_csv_products()
    except FileNotFoundError:
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
    app.run(debug=True, port=5000)
