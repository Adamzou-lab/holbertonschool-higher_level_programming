#!/usr/bin/python3
"""Flask application rendering a dynamic list of items from JSON."""
import json

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Render the items page with a list of items read from items.json."""
    try:
        with open('items.json') as items_file:
            data = json.load(items_file)
            item_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        item_list = []

    return render_template('items.html', items=item_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
