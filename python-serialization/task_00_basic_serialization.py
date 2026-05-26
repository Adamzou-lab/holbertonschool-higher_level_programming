#!/usr/bin/env python3
"""Module that provides basic JSON serialization and
deserialization functions."""

import json


def serialize_and_save_to_file(data, filename):
    """Serializes a Python dictionary and saves it to a JSON file."""
    with open(filename, "w") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Loads and deserializes a JSON file into a Python dictionary."""
    with open(filename, "r") as f:
        data = json.load(f)
    return data
