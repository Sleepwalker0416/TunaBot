#Tuna Bot Main
import discord
import os
from itertools import cycle
from discord.ext import commands, tasks
from discord.ext.commands.errors import MissingRequiredArgument

client = commands.Bot(command_prefix = 't')

#Status cycle   
status = cycle(['Bullying everyone!', 'Taste the salt!'])

#Ready check
@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready!')

#Tasks
@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(next(status)))

@client.command()
async def load(ctx, extension):
    client.load_extension(f'Cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'Cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'Cogs.{extension}')
    client.load_extension(f'Cogs.{extension}')

for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'Cogs.{filename[:-3]}')

client.run('')