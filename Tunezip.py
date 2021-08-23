import discord
from discord import Activity, ActivityType 
from discord.ext import commands, tasks

import json
from pathlib import Path
import os

import src.json

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}")

def prefix(bot, message):
    data = src.json.read_json('prefixes')
    if not str(message.guild.id) in data:
        return commands.when_mentioned_or('+')(bot, message)
    return commands.when_mentioned_or(data[str(message.guild.id)])(bot, message)

token_file = json.load(open(cwd+'/config/donttouch.json'))
tunezip = commands.Bot(command_prefix= prefix, intents = discord.Intents.all(), case_insensitive= True)
tunezip.config_token = token_file['token']

@tunezip.event
async def on_ready():
    print(f"-----\n Logged in as: {tunezip.user.name} : {tunezip.user.id}\n-----\n Current prefix: +\n-----")
    await tunezip.change_presence(activity=Activity(name=f"In development",
                                                type=ActivityType.playing))

@tunezip.event
async def on_message(message):
    if message.author.id == tunezip.user.id:
        return

    await tunezip.process_commands(message)

tunezip.remove_command('help')

if __name__ == '__main__':
    for file in os.listdir(cwd+"/src/cogs/config"):
        if file.endswith(".py") and not file.startswith("_"):
            tunezip.load_extension(f"src.cogs.config.{file[:-3]}")

if __name__ == '__main__':
    for file in os.listdir(cwd+"/src/cogs/fun"):
        if file.endswith(".py") and not file.startswith("_"):
            tunezip.load_extension(f"src.cogs.fun.{file[:-3]}")

if __name__ == '__main__':
    for file in os.listdir(cwd+"/src/cogs/images"):
        if file.endswith(".py") and not file.startswith("_"):
            tunezip.load_extension(f"src.cogs.images.{file[:-3]}")

if __name__ == '__main__':
    for file in os.listdir(cwd+"/src/cogs/misc"):
        if file.endswith(".py") and not file.startswith("_"):
            tunezip.load_extension(f"src.cogs.misc.{file[:-3]}")

if __name__ == '__main__':
    for file in os.listdir(cwd+"/src/cogs/moderation"):
        if file.endswith(".py") and not file.startswith("_"):
            tunezip.load_extension(f"src.cogs.moderation.{file[:-3]}")

if __name__ == '__main__':
    for file in os.listdir(cwd+"/src/cogs/music"):
        if file.endswith(".py") and not file.startswith("_"):
            tunezip.load_extension(f"src.cogs.music.{file[:-3]}")

tunezip.run(tunezip.config_token)