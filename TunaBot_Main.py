#Tuna Bot
import discord
import os
from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument

client = commands.Bot(command_prefix = 't')

#Ready check
@client.event
async def on_ready():
    print('Bot is ready!')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('.\cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('ODkxMTc4OTAyMzA5OTc4MTIz.YU6lBw.P_K-d_2fc_y0mjdRYMaE5-sUM_k')