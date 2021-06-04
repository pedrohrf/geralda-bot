import discord
import src.enums.system_variables as sv
from src.on_message import execute
from src.helpers.discord_response import response

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user or message.channel.name != sv.DISCORD_CHANNEL:  # This line avoids loops
        return
    try:
        await response(await execute(message.content), message)
    except Exception as e:
        await response(e, message)


client.run(sv.DISCORD_TOKEN)
