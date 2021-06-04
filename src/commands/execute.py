from src.exceptions import InvalidCommand
from src.commands.graph import Graph


class Execute:
    """
    **Execute: Executa o comando de um gráfico previamente salvo**
    - Line 1: !execute
    - Line 2: <label>
    **Resultado: Imagem de um gráfico**
    """

    def __init__(self, message_content):
        try:
            self.query, self.label = message_content.split("\n")
        except Exception:
            raise InvalidCommand()

    def __call__(self):
        f = open(f"saved/{self.label}.grd", "r")
        graph = Graph(f.read())
        return graph()
