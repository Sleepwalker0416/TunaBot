#Tuna Bot
import discord
from discord.ext import commands, tasks
from itertools import cycle
from discord.ext.commands.errors import MissingRequiredArgument

client = commands.Bot(command_prefix = 't')
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

#Errors
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command!')

#Command
#Reaction command
@client.command()
async def ping(ctx):
    await ctx.send(f'Ping: {round(client.latency * 1000)} ms')

@client.command()
async def Tuna(ctx):
    await ctx.send('Cuncec gì UwU')

#Moderation command
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)
    await ctx.send(str(amount) + ' cleared messages')

#Clear error
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Invalid argument!')

client.run('')