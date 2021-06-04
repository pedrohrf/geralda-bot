from src.exceptions import InvalidCommand


class Load:
    """
    **Load: Carrega o comando previamente salvo**
    - Line 1: !load
    - Line 2: <label>
    **Resultado: Comando !graph**
    """

    def __init__(self, message_content):
        try:
            self.query, self.label = message_content.split("\n")
        except Exception:
            raise InvalidCommand()

    def __call__(self):
        f = open(f"saved/{self.label}.grd", "r")
        return f.read()
