#!/usr/bin/python3
"""Display products from JSON, CSV and SQLite sources."""

import csv
import json
import os
import sqlite3
from contextlib import closing
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json():
    """Read products from JSON."""
    path = os.path.join(app.root_path, 'products.json')

    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


def read_csv():
    """Read products from CSV."""
    path = os.path.join(app.root_path, 'products.csv')

    with open(path, 'r', encoding='utf-8', newline='') as file:
        return list(csv.DictReader(file))


def read_sql():
    """Read products from the SQLite database."""
    path = os.path.join(app.root_path, 'products.db')

    if not os.path.isfile(path):
        raise sqlite3.OperationalError('Database file not found')

    with closing(sqlite3.connect(path)) as conn:
        conn.row_factory = sqlite3.Row

        cursor = conn.execute(
            'SELECT id, name, category, price FROM Products ORDER BY id'
        )

        return [dict(row) for row in cursor.fetchall()]


@app.route('/products')
def products():
    """Display products from the selected data source."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    try:
        if source == 'json':
            data = read_json()

        elif source == 'csv':
            data = read_csv()

        elif source == 'sql':
            data = read_sql()

        else:
            return render_template(
                'product_display.html', error="Wrong source"
            )

    except sqlite3.Error:
        return render_template(
            'product_display.html', error="Database error"
        )

    except (OSError, ValueError, csv.Error):
        return render_template(
            'product_display.html', error="Error reading data"
        )

    if product_id is not None:
        data = [
            product for product in data
            if str(product['id']) == product_id
        ]

        if not data:
            return render_template(
                'product_display.html', error="Product not found"
            )

    return render_template(
        'product_display.html', products=data
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
