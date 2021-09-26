#Tuna Bot Commands
import discord
from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument

class Command(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    #Command
    #Reaction command
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Ping: {round(self.client.latency * 1000)} ms')

    @commands.command()
    async def Tuna(self, ctx):
        await ctx.send('Cuncec gì UwU')

    #Moderation command
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)
        await ctx.send(str(amount) + ' cleared messages')

    #Clear error
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Invalid argument!')

def setup(client):
    client.add_cog(Command(client))