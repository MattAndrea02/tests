# File pieno di bug e hotspot per test SonarQube

def divisione(a, b):
    # Possibile divisione per zero (bug)
    return a / b


def password_check(password):
    # Hardcoded password (security hotspot)
    if password == "123456":
        return True
    return False


def sql_injection(user_input):
    # SQL Injection (security hotspot)
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    return query


def unused_variable():
    # Variabile non usata (code smell)
    x = 42
    return True


def infinite_loop():
    # Loop infinito (bug)
    while True:
        pass


def deprecated_function():
    # Uso di funzione deprecata (bug/hotspot)
    import imp
    imp.reload(__import__('math'))


def insecure_hash(data):
    # Uso di algoritmo di hash insicuro (security hotspot)
    import hashlib
    return hashlib.md5(data.encode()).hexdigest()


def open_file_without_close(filename):
    # File non chiuso correttamente (bug)
    f = open(filename, 'r')
    data = f.read()
    return data


def catch_all_exception():
    # Catch generico (code smell)
    try:
        1 / 0
    except Exception:
        return 'errore'


def assert_used_in_production(x):
    # Uso improprio di assert (bug/hotspot)
    assert x > 0
    return x
