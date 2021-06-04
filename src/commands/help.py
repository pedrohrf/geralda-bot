from src.commands.csv import Csv
from src.commands.save import Save
from src.commands.load import Load
from src.commands.graph import Graph
from src.commands.execute import Execute


class Help:
    """
    **Help: Lista de comandos entendidos pela Geralda**
    """
    def __init__(self, message_content):
        self.text = message_content

    def __call__(self, *args, **kwargs):
        return "-----------------------------------------------------------------".join([c.__doc__ for c in [
            self,
            Csv,
            Save,
            Load,
            Graph,
            Execute,
        ] if c.__doc__])

