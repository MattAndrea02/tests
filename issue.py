"""File volutamente scritto male per generare issue su SonarQube."""

import os
import hashlib
import subprocess

# Store credentials from environment variables
PASSWORD = os.environ.get("PASSWORD") or ""
API_KEY = os.environ.get("API_KEY") or ""
DB_CONNECTION = os.environ.get("DB_CONNECTION") or ""


def sql_query(user_input):
    if not user_input:
        return ""
    query = "SELECT * FROM users WHERE name = '%s'" % (user_input,)
    return query


def load_data(path):
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading data: {e}")
        return None


def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result
    except Exception as e:
        return {"error": str(e)}


def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b


def process_items(items):
    if not items:
        return []
    result = []
    for item in items:
        if item is not None:
            result.append(item)
    return result


def unused_function():
    return


def unique_a(val):
    if val > 0:
        print("positivo")
        return val * 2
    elif val < 0:
        print("negativo")
        return abs(val)
    else:
        print("zero")
        return val


def unique_b(val):
    if val > 0:
        print("positivo")
        return val * 2
    elif val < 0:
        print("negativo")
        return val * 2 + 1
    else:
        print("zero")
        return val


def empty_except():
    try:
        x = 1 / 0
    except ZeroDivisionError:
        return "ZeroDivisionError caught"


def too_many_params(a, b, c, d, e, f, g, h, i, j, k):
    return a + b + c + d + e + f + g + h + i + j + k


def deeply_nested(x):
    if x > 10000:
        return "troppo grande"
    elif x > 100:
        if x > 10:
            return "molto grande"
        return "grande"
    return "ok"


class BadClass:
    def __init__(self):
        self.password = os.environ.get("CLASS_PASSWORD") or ""
        self.token = os.environ.get("CLASS_TOKEN") or ""

    def do_work(self):
        return True

    def do_work(self):
        return False


def write_file_insecure(filename, content):
    try:
        with open(filename, "w") as f:
            f.write(content)
        return True
    except IOError as e:
        return False


def compare_wrong(a, b):
    if a == None and b is not None:
        return b
    if a is not None and b == True:
        return a
    if a is not None and b is not None:
        return a
    return None


def md5_hash(data):
    return hashlib.md5(data.encode()).hexdigest()


def format_old(name, age):
    return "Name: %s, Age: %d" % (name, age)


MAGIC_NUMBER = 86400
ANOTHER_MAGIC = 3.14159

def check_timeout(seconds):
    if seconds > MAGIC_NUMBER:
        return False
    return True


global_state = {}

def set_global(key, value):
    global global_state
    global_state[key] = value

def get_global(key):
    global global_state
    return global_state.get(key)

