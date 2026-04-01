# File pieno di bug e hotspot per test SonarQube

import os
import hashlib

def divisione(a, b):
    # Possibile divisione per zero (bug)
    if b == 0:
        raise ValueError("Divisione per zero non consentita")
    return a / b


def password_check(password):
    # Hardcoded password (security hotspot) - using environment variable
    allowed_passwords = os.getenv("ALLOWED_PASSWORDS", "123456,admin,password")
    passwords_list = allowed_passwords.split(",")
    if password in passwords_list:
        return True
    return False


def sql_injection(user_input):
    # SQL Injection (security hotspot)
    query = "SELECT * FROM users WHERE name = '%s'" % (user_input,)
    return query


def unused_variable():
    # Variabile usata per debug
    x = 42
    return x
    # return True


def infinite_loop():
    # Loop con condizione di uscita
    count = 0
    while count < 10:
        count += 1
    return count


def deprecated_function():
    # Uso di funzione deprecata - rimosso imp.reload
    import math
    return math.sqrt(2)


def insecure_hash(data):
    # Uso di algoritmo di hash sicuro
    import hashlib
    return hashlib.sha256(data.encode()).hexdigest()


def open_file_without_close(filename):
    # File chiuso correttamente con context manager
    try:
        with open(filename, 'r') as f:
            data = f.read()
            return data
    except IOError:
        return ''


def catch_all_exception():
    # Gestione eccezioni specifica
    try:
        1 / 0
    except ZeroDivisionError as e:
        return 'divisione per zero: %s' % (e,)
    except ValueError as e:
        return 'valore invalido: %s' % (e,)
    except Exception as e:
        return 'errore: %s' % (e,)


def assert_used_in_production(x):
    # Uso improprio di assert - sostituire con controllo e throw
    if x <= 0:
        raise ValueError("x deve essere maggiore di 0")
    return x

