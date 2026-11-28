#!/usr/bin/python3
"""Flask application for displaying JSON and CSV product data."""

import csv
import json
import os
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json():
    """Read products from a JSON file."""
    path = os.path.join(app.root_path, 'products.json')

    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


def read_csv():
    """Read products from a CSV file."""
    path = os.path.join(app.root_path, 'products.csv')

    with open(path, 'r', encoding='utf-8', newline='') as file:
        return list(csv.DictReader(file))


@app.route('/products')
def products():
    """Display products from the selected data source."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    else:
        return render_template(
            'product_display.html', error="Wrong source"
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
