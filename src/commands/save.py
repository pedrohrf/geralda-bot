from src.exceptions import InvalidCommand
from src.enums.messages import COMMAND_SAVED_FEEDBACK
from src.commands.graph import Graph


class Save:
    """
    **Save: Salva um comando graph para ser posteriormente invocado**
    - Line 1: !save
    - Line 2: <label>
    - Line 3: A Select for database
    - Line 4: graph seaborn format
    - Line 5: graph args
    """

    def __init__(self, message_content):
        try:
            _, self.label, self.query, self.format, self.args = message_content.split("\n")
            self.graph_command = "\n".join(["!graph", self.query, self.format, self.args])
        except Exception:
            raise InvalidCommand()

    def __call__(self):
        graph = Graph(self.graph_command)
        graph()
        f = open(f"saved/{self.label}.grd", "w")
        f.write(self.graph_command)
        return COMMAND_SAVED_FEEDBACK
