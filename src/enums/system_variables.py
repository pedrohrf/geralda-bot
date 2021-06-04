import os

TOKEN = os.environ.get('DISCORD_TOKEN')
DB_CREDENTIALS = {
    'host': os.environ.get('DB_HOST', "172.17.0.4"),
    'database': os.environ.get('DB_NAME', 'postgres'),
    'user': os.environ.get('DB_USER', 'postgres'),
    'password': os.environ.get('DB_PWD', 'mysecretpassword'),
    'port': os.environ.get('DB_PORT', '5432')
}
