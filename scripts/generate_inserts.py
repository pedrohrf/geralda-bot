import random

for x in range(0, 100000):
    method_name = f"'method_name_{random.randint(1, 10)}'"
    sucess = "true" if random.randint(0, 1) == 1 else "false"
    duration = f"{random.randint(1, 60)}"
    creation_date = f"'202{random.randint(0, 1)}-{random.randint(1, 12)}-{random.randint(1, 28)}'"
    message = f"'message {random.randint(0, 100)}'"
    values = f"({method_name}, {sucess}, {duration}, {creation_date}, {message})"
    print(f"INSERT INTO metrics (method_name, sucess, duration, creation_date, message) VALUES {values};")
