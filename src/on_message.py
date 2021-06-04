from src.commands import commands

commands_map = {}
for command in commands:
    commands_map[f"!{command.__name__.lower()}"] = command


async def execute(message_content):
    def get_command_from_message_content() -> str:
        return message_content.split("\n")[0].split(" ")[0]

    cmd = commands_map[get_command_from_message_content()](message_content)
    return cmd()
