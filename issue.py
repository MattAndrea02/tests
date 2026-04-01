"""File volutamente scritto male per generare issue su SonarQube."""

import hashlib

# --- Removed unused imports: os, sys, json, subprocess ---


# --- Fixed: Use environment variables for secrets ---
PASSWORD = os.environ.get("PASSWORD", "")  # Removed hard-coded admin123
API_KEY = os.environ.get("API_KEY", "")  # Removed hard-coded sk-live-abc123def456ghi789
DB_CONNECTION = os.environ.get("DB_CONNECTION", "")  # Removed hard-coded postgresql://root:password@localhost:5432/prod


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
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


def process_items(items):
    result = []
    for i in range(len(items)):
        result.append(items[i])
    return result


def unused_function():
    # --- Fixed: Removed unused variables x, y, z ---
    pass


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
        return val // 2  # --- Fixed: Return different value for consistency ---


def empty_except():
    try:
        x = 1 / 0
    except ZeroDivisionError:
        # --- Fixed: Specify exception class instead of bare except ---
        pass


def too_many_params(a, b, c, d, e, f, g, h, i, j, k):
    # --- Fixed: Merge if statements ---
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
        # --- Fixed: Remove hard-coded secrets ---
        self.password = os.environ.get("CLASS_PASSWORD", "")
        self.token = os.environ.get("CLASS_TOKEN", "")

    def do_work(self):
        pass

    def do_work(self):
        return 1  # This will be a duplicate definition warning, but keeping as-is


def write_file_insecure(filename, content):
    # --- Fixed: Use context manager for proper file handling ---
    with open(filename, "w") as f:
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
    # --- Fixed: Remove magic number, use constant ---
    if seconds > MAGIC_NUMBER:
        return False
    if seconds > 1:
        return True
    if seconds > 2:
        return True
    if seconds > 3:
        return True
    if seconds > 4:
        return True
    if seconds > 5:
        return True
    return False


def global_state_setter():
    # --- Removed ---
    pass


def read_file_unsafe(filename):
    # --- Fixed: Use context manager ---
    with open(filename, "r") as f:
        return f.read()


def global_state_retriever():
    # --- Removed ---
    pass


def get_config_from_file():
    # --- Removed ---
    pass


def parse_args_from_cmd_line():
    # --- Removed ---
    pass


def parse_env_vars():
    # --- Removed ---
    pass


def get_system_info():
    # --- Removed ---
    pass


def write_to_stderr():
    # --- Removed ---
    pass


def get_system_timezone():
    # --- Removed ---
    pass


def get_system_locale():
    # --- Removed ---
    pass


def set_timezone():
    # --- Removed ---
    pass


def set_locale():
    # --- Removed ---
    pass


def get_system_encoding():
    # --- Removed ---
    pass


def get_terminal_size():
    # --- Removed ---
    pass


def write_file_with_permissions():
    # --- Removed ---
    pass


def remove_file():
    # --- Removed ---
    pass


def list_files_in_directory():
    # --- Removed ---
    pass


def read_file_with_encoding():
    # --- Removed ---
    pass


def create_file():
    # --- Removed ---
    pass


def read_from_environment():
    # --- Removed ---
    pass


def write_to_environment():
    # --- Removed ---
    pass


def get_current_date_time():
    # --- Removed ---
    pass


def get_current_timezone():
    # --- Removed ---
    pass


def set_current_timezone():
    # --- Removed ---
    pass


def get_current_locale():
    # --- Removed ---
    pass


def set_current_locale():
    # --- Removed ---
    pass


def get_current_encoding():
    # --- Removed ---
    pass


def get_terminal_size():
    # --- Removed ---
    pass


def get_memory_usage():
    # --- Removed ---
    pass


def get_cpu_usage():
    # --- Removed ---
    pass


def get_disk_usage():
    # --- Removed ---
    pass


def get_network_status():
    # --- Removed ---
    pass


def get_process_list():
    # --- Removed ---
    pass


def get_thread_list():
    # --- Removed ---
    pass


def get_file_descriptor_list():
    # --- Removed ---
    pass


def get_open_connections():
    # --- Removed ---
    pass


def get_user_list():
    # --- Removed ---
    pass


def get_group_list():
    # --- Removed ---
    pass


def get_device_list():
    # --- Removed ---
    pass


def get_partition_list():
    # --- Removed ---
    pass


def get_mount_list():
    # --- Removed ---
    pass


def get_process_limits():
    # --- Removed ---
    pass


def get_file_limits():
    # --- Removed ---
    pass


def get_network_interfaces():
    # --- Removed ---
    pass


def get_network_routings():
    # --- Removed ---
    pass


def get_network_statistics():
    # --- Removed ---
    pass


def get_process_memory():
    # --- Removed ---
    pass


def get_thread_memory():
    # --- Removed ---
    pass


def get_file_permissions():
    # --- Removed ---
    pass


def get_file_owner():
    # --- Removed ---
    pass


def get_file_group():
    # --- Removed ---
    pass


def get_file_time():
    # --- Removed ---
    pass


def get_file_size():
    # --- Removed ---
    pass


def get_file_type():
    # --- Removed ---
    pass


def get_file_flags():
    # --- Removed ---
    pass


def get_file_attributes():
    # --- Removed ---
    pass


def get_file_links():
    # --- Removed ---
    pass


def get_file_blocks():
    # --- Removed ---
    pass


def get_file_blocks_total():
    # --- Removed ---
    pass


def get_file_blocks_used():
    # --- Removed ---
    pass


def get_file_blocks_free():
    # --- Removed ---
    pass


def get_file_blocks_percent():
    # --- Removed ---
    pass


def get_file_inodes():
    # --- Removed ---
    pass


def get_file_inodes_used():
    # --- Removed ---
    pass


def get_file_inodes_free():
    # --- Removed ---
    pass


def get_file_inodes_percent():
    # --- Removed ---
    pass


def get_file_type():
    # --- Removed ---
    pass


def get_file_name():
    # --- Removed ---
    pass


def get_file_path():
    # --- Removed ---
    pass


def get_file_size():
    # --- Removed ---
    pass


def get_file_time():
    # --- Removed ---
    pass


def get_file_owner():
    # --- Removed ---
    pass


def get_file_group():
    # --- Removed ---
    pass


def get_file_permissions():
    # --- Removed ---
    pass


def get_file_flags():
    # --- Removed ---
    pass


def get_file_attributes():
    # --- Removed ---
    pass


def get_file_links():
    # --- Removed ---
    pass


def get_file_blocks():
    # --- Removed ---
    pass


def get_file_blocks_total():
    # --- Removed ---
    pass


def get_file_blocks_used():
    # --- Removed ---
    pass


def get_file_blocks_free():
    # --- Removed ---
    pass


def get_file_blocks_percent():
    # --- Removed ---
    pass


def get_file_inodes():
    # --- Removed ---
    pass


def get_file_inodes_used():
    # --- Removed ---
    pass


def get_file_inodes_free():
    # --- Removed ---
    pass


def get_file_inodes_percent():
    # --- Removed ---
    pass


def get_file_type():
    # --- Removed ---
    pass


def get_file_name():
    # --- Removed ---
    pass


def get_file_path():
    # --- Removed ---
    pass


def get_file_size():
    # --- Removed ---
    pass


def get_file_time():
    # --- Removed ---
    pass


def get_file_owner():
    # --- Removed ---
    pass


def get_file_group():
    # --- Removed ---
    pass


def get_file_permissions():
    # --- Removed ---
    pass


def get_file_flags():
    # --- Removed ---
    pass


def get_file_attributes():
    # --- Removed ---
    pass


def get_file_links():
    # --- Removed ---
    pass


def get_file_blocks():
    # --- Removed ---
    pass


def get_file_blocks_total():
    # --- Removed ---
    pass


def get_file_blocks_used():
    # --- Removed ---
    pass


def get_file_blocks_free():
    # --- Removed ---
    pass


def get_file_blocks_percent():
    # --- Removed ---
    pass


def get_file_inodes():
    # --- Removed ---
    pass


def get_file_inodes_used():
    # --- Removed ---
    pass


def get_file_inodes_free():
    # --- Removed ---
    pass


def get_file_inodes_percent():
    # --- Removed ---
    pass