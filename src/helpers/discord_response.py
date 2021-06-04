import discord
from functools import singledispatch
from src.commands.graph import Graph
from src.commands.csv import Csv
from src.exceptions import BaseDiscordResponseException
from src.enums.messages import ERROR_BASE_MESAGE, GENERIC_ERROR, INVALID_COMMAND


@singledispatch
async def response(x, message):
    raise NotImplementedError


@response.register(Graph)
async def response_graph(graph: Graph, message):
    await message.channel.send(file=discord.File(graph.file_name))


@response.register(Csv)
async def response_graph(csv: Csv, message):
    await message.channel.send(file=discord.File(csv.file_name))


@response.register(str)
async def response_str(_str: str, message):
    await message.channel.send(_str)


@response.register(BaseDiscordResponseException)
async def response_base_discord_response_exception(exept: BaseDiscordResponseException, message):
    await message.channel.send(f"{ERROR_BASE_MESAGE} {message.author}\n{exept.message}")


@response.register(KeyError)
async def response_exception(_: KeyError, message):
    await message.channel.send(f"{ERROR_BASE_MESAGE} {message.author}\n{INVALID_COMMAND}")


@response.register(Exception)
async def response_exception(_: Exception, message):
    await message.channel.send(f"{ERROR_BASE_MESAGE} {message.author}\n{GENERIC_ERROR}")

