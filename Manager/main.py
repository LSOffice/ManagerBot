import discord
import os
import time, random, datetime, json, asyncio

from discord import Spotify, Status
from discord.ext import commands
from discord.utils import get
from get_token import token
from log.logger import Log
from itertools import cycle

async def is_guild_owner(ctx):
    return ctx.author.id == ctx.guild.owner.id

def get_prefix(bot, message):
    if not message.guild:
        return commands.when_mentioned_or("!")(bot, message)

    with open("./settings/prefix.json", "r") as f:
        prefixes = json.load(f)

    if str(message.guild.id) not in prefixes:
        return commands.when_mentioned_or("!")(bot, message)

    prefix = prefixes[str(message.guild.id)]
    return commands.when_mentioned_or(prefix)(bot, message)

client = commands.Bot(command_prefix=get_prefix, case_insensitive=False)
client.remove_command('help')

async def chng_pr():
    await client.wait_until_ready()

    statuses = ['!help', 'with new commands', 'with theManager wiki', 'Manager.io', f"with {client.user}'s code", "Manager 101 on Spotify"]
    statuses = cycle(statuses)

    while not client.is_closed():
        status = next(statuses)
        Log(status='chng_pr', activity='Playing', new_presence=status)
        await client.change_presence(activity=discord.Game(status))
        await asyncio.sleep(30)

async def ping_alert():
    await client.wait_until_ready()

    while not client.is_closed():
        ping = round(client.latency*1000)
        channel = client.get_channel(752355253395128341)
        if ping >= 200:
            await channel.send(f"**ALERT: ** High Ping!\nPing: {ping}")
        elif ping <= 20:
            await channel.send(f"**Nice! ** Low Ping!\nPing: {ping}")

        await asyncio.sleep(60)

for cog in os.listdir("./cogs"):
    if cog.endswith(".py"):
        try:
            cog = f"cogs.{cog.replace('.py', '')}"
            client.load_extension(cog)
            print(f"Loaded {cog}.")
            Log(status="CogSuccess", cogname=cog)
        except Exception as e:
            print(f"{cog} cannot be loaded.")
            Log(status="CogFail", errono=3, cogname=cog)
            raise e

client.loop.create_task(chng_pr())
client.loop.create_task(ping_alert())
client.run(token)