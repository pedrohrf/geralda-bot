from src.exceptions import InvalidCommand
from src.helpers.postgresql import Postgresql
from src.enums.system_variables import DB_CREDENTIALS
from datetime import datetime
import seaborn as sns
import json


class Graph:
    """
    **Graph: Executa um select e monta um grafico**
    - Line 1: !graph
    - Line 2: A Select for database
    - Line 3: graph seaborn format
    - Line 4: graph args
    **Resultado: Imagem de um gráfico**
    """

    def __init__(self, message_content):
        try:
            sns.set_theme()
            lines = message_content.split("\n")
            self.query = lines[1]
            self.plot = getattr(sns, lines[2])
            self.args = json.loads(lines[3])
            self.file_name = f"graphs/{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        except Exception:
            raise InvalidCommand()

    def __call__(self):
        db = Postgresql(**DB_CREDENTIALS)
        sns_plot = self.plot(data=db.query(self.query), **self.args)
        sns_plot.savefig(self.file_name)
        return self

