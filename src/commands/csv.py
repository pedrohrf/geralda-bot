from src.enums.system_variables import DB_CREDENTIALS
from src.exceptions import InvalidCommand
from src.helpers.postgresql import Postgresql
from datetime import datetime


class Csv:
    """
    **Csv: Executa um select**
    - Line 1: !csv
    - Line 2: A Select for database
    **Resultado: Arquivo csv**
    """

    def __init__(self, message_content):
        try:
            lines = message_content.split("\n")
            self.query = lines[1]
            self.file_name = f"csv/{datetime.now().strftime('%Y%m%d%H%M%S')}.csv"
        except Exception:
            raise InvalidCommand()

    def __call__(self):
        db = Postgresql(**DB_CREDENTIALS)
        f = open(self.file_name, 'w')
        f.write(db.query(self.query).to_csv())
        return self
