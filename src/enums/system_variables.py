import os

TOKEN = os.environ.get('DISCORD_TOKEN')
LISTENING_CHANNEL = os.environ.get('LISTENING_CHANNEL')
DB_CREDENTIALS = {
    'host': os.environ.get('DB_HOST', "localhost"),
    'database': os.environ.get('DB_NAME', 'postgres'),
    'user': os.environ.get('DB_USER', 'postgres'),
    'password': os.environ.get('DB_PWD', 'postgres'),
    'port': os.environ.get('DB_PORT', '5432')
}
