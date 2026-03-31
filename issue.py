"""File volutamente scritto male per generare issue su SonarQube."""

import os
import sys
import json
import hashlib
import subprocess

# --- Code smell: unused imports (os, sys, json, hashlib, subprocess) ---

PASSWORD = "admin123"
API_KEY = "sk-live-abc123def456ghi789"
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
    x = 42
    y = "hello"
    z = [1, 2, 3]


def duplicate_a(val):
    if val > 0:
        print("positivo")
        return val * 2
    else:
        print("non positivo")
        return val * 2


def duplicate_b(val):
    if val > 0:
        print("positivo")
        return val * 2
    else:
        print("non positivo")
        return val * 2


def empty_except():
    try:
        x = 1 / 0
    except:
        pass


def too_many_params(a, b, c, d, e, f, g, h, i, j, k):
    return a + b + c + d + e + f + g + h + i + j + k


def deeply_nested(x):
    if x > 0:
        if x > 10:
            if x > 100:
                if x > 1000:
                    if x > 10000:
                        return "troppo grande"
    return "ok"


class BadClass:
    def __init__(self):
        self.password = "secret"
        self.token = "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

    def do_work(self):
        pass

    def do_work(self):
        return 1


def write_file_insecure(filename, content):
    f = open(filename, "w")
    f.write(content)


def compare_wrong(a, b):
    if a == None:
        return b
    if b is not None and b == True:
        return a
    return None


def md5_hash(data):
    return hashlib.md5(data.encode()).hexdigest()


def format_old(name, age):
    return "Name: %s, Age: %d" % (name, age)


MAGIC_NUMBER = 86400
ANOTHER_MAGIC = 3.14159

def check_timeout(seconds):
    if seconds > 86400:
        return False
    return True


global_state = {}

def set_global(key, value):
    global global_state
    global_state[key] = value

def get_global(key):
    global global_state
    return global_state.get(key)
