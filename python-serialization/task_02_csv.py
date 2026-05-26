#!/usr/bin/env python3
"""Module that converts CSV data to JSON format."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Converts a CSV file to JSON format and saves it to data.json."""
    try:
        with open(csv_filename, "r") as f:
            reader = csv.DictReader(f)
            data = list(reader)
    except Exception:
        return False

    with open("data.json", "w") as f:
        try:
            json.dump(data, f)
            return True
        except Exception:
            return False
