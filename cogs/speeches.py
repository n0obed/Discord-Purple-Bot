import discord
from discord.ext import commands
import random

class speeches(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    # events
    #@commands.Cog.listener()
    
    # commands
    @commands.command(aliases = ['hello','hey'])
    async def hi(self, ctx):
        hi = ['hi there.', 'hello', 'Whats up dude!', 'How ya doing!',
        'heyy', 'Yo!', 'Hey buddy!']
        await ctx.send(f'{random.choice(hi)}')
    
    @commands.command(aliases = ['LAUGH'] )
    async def laugh(self, ctx):
        await ctx.send('MUAHAHAH!!!')
        await ctx.message.delete()

    @commands.command(aliases = ['NOOBED'])
    async def  noobed(self, ctx):
        await ctx.send('@n0obed you there?')
        await time.sleep(2)
        await ctx.message.delete()
        await ctx.send('noobed is busy right now contact him later.')
    
    @commands.command(aliases = ['test'] )
    async def g(self, ctx):
        await ctx.send('-p nf time')


def setup(client):
    client.add_cog(speeches(client))













