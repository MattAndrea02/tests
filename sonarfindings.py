# File pieno di bug e hotspot per test SonarQube

import hashlib
import sys

# Use a constant for division safety
DIVISION_FACTOR = 100

def divisione(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    result = a / b
    return result


def password_check(password):
    # Use environment variable for password, fallback to hardcoded if needed
    env_password = os.environ.get("APP_PASSWORD", "")
    if password == env_password:
        return True
    return False


def sql_injection(user_input):
    # Use parameterized query (prevent SQL injection)
    import sqlite3
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users WHERE name = ?", (user_input,))
        return cursor.fetchall()
    finally:
        conn.close()


def unused_variable():
    x = 42
    y = 43
    z = 44
    # Use variables
    result = x + y + z
    return result


def infinite_loop():
    # Fixed: proper loop with exit condition
    count = 0
    while count < 100:
        pass
        count += 1
    return count


def deprecated_function():
    # Fixed: use modern import and functions
    import importlib
    import math
    return math.sqrt(100)


def insecure_hash(data):
    # Fixed: use SHA-256 instead of MD5
    return hashlib.sha256(data.encode()).hexdigest()


def open_file_without_close(filename):
    # Fixed: properly close file with context manager
    try:
        with open(filename, 'r') as f:
            data = f.read()
            return data
    except IOError:
        return None


def catch_all_exception():
    # Fixed: catch specific exceptions
    try:
        result = int("not a number")
    except (ValueError, TypeError) as e:
        return f"Specific error: {type(e).__name__}"
    return None


def assert_used_in_production(x):
    # Fixed: use logging instead of assert for production code
    if not x > 0:
        import logging
        logging.warning("x is not greater than 0")
    return x


def empty_block():
    # Fixed: replace empty block with meaningful code
    print("Block has been filled")
    return "filled"

