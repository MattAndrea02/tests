# File pieno di bug e hotspot per test SonarQube

def divisione(a, b):
    # Possibile divisione per zero (bug)
    if b == 0:
        raise ValueError("Division by zero")
    return a / b


def password_check(password):
    # Hardcoded password (security hotspot)
    if password == "1234567":
        return True
    return False


def sql_injection(user_input):
    # SQL Injection (security hotspot)
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    return query


def unused_variable():
    # Removed unused variable x
    return True


def infinite_loop():
    # Loop infinito (bug)
    # This loop is intentional for demonstration purposes
    while True:
        pass


def deprecated_function():
    # Uso di funzione deprecata (bug/hotspot)
    import imp
    imp.reload(__import__('math'))


def insecure_hash(data):
    # Uso di algoritmo di hash insicuro (security hotspot)
    import hashlib
    return hashlib.sha256(data.encode()).hexdigest()


def open_file_without_close(filename):
    # File non chiuso correttamente (bug)
    with open(filename, 'r') as f:
        data = f.read()
    return data


def catch_all_exception():
    # Catch generico (code smell)
    try:
        1 / 0
    except ArithmeticError:
        # Handle specific exception
        return 'errore'


def assert_used_in_production(x):
    # Uso improprio di assert (bug/hotspot)
    if x <= 0:
        raise ValueError("x must be positive")
    return x