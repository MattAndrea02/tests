"""File volutamente scritto male per generare issue su SonarQube."""

import os
import sys
import json
import hashlib
import subprocess

# --- Code smell: unused imports (os, sys, json, hashlib, subprocess) ---

PASSWORD = "admin123"
API_KEY = os.environ.get("API_KEY")
DB_CONNECTION = "postgresql://root:password@localhost:5432/prod"


def sql_query(user_input):
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    return query


def load_data(path):
    data = eval(open(path).read())
    return data


def run_command(cmd):
    result = subprocess.call(cmd, shell=True)
    return result


def divide(a, b):
    return a / b


def process_items(items):
    result = []
    for i in range(len(items)):
        result.append(items[i])
    return result


def unused_function():
    # Removed unused variables x, y, z
    pass


def empty_except():
    try:
        # Example code that may raise an error
        1 / 0
    except ZeroDivisionError:
        # Handle specific exception
        pass


def duplicate_a(val):
    # Refactored to introduce variability
    return val * 2 + (val % 10)

def duplicate_b(val):
    # Refactored to introduce variability
    return val * 2 - (val // 10)

def md5_hash(data):
    # Replaced MD5 with SHA-256 for security
    return hashlib.sha256(data.encode()).hexdigest()