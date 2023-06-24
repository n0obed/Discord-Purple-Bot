import discord
from discord.ext import commands, tasks
from itertools import cycle
import time
import random
import os

client = commands.Bot(command_prefix='/')

def check_if_its_me(ctx):
    return ctx.message.author.id == 351949188323475457
def check_if_its_exam(ctx):
    exam_list = [775045105660723210, 775045234265686036, 775045487736520705, 775045648142958643]
    for id in exam_list:
        if ctx.message.channel.id == id:
            return True
        else:
            return False
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension})')
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension})')
@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension})')
    client.load_extension(f'cogs.{extension})')

for filename in os.listdir('./cogs'): # '.' represents current directory
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
    





diff_status = cycle([ 'nothin cuz i am Bored af', 'Nothing', 'songs cuz bots like songs'])
@tasks.loop(seconds = 10)
async def change_status_loop():
    await client.change_presence(activity = discord.Game(next(diff_status) ))



@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online)
    change_status_loop.start()


@client.event
async def on_connect():
    print('Hey I am ready', f'logged in as {client.user}')


f = open('filtered_words.txt','r')
empty = []
filtered_words = f.read().split()
@client.event
async def on_message(msg):
    for word in empty: #filtered_words:
        if word == msg.content:
            await msg.delete()        
    await client.process_commands(msg)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error,commands.CommandNotFound):
        await ctx.send('I dont have a command like that /help might help you')
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send('You do not have permission to kick') 
        time.sleep(4)
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Some arguments are missing' )
        time.sleep(4)
        await ctx.message.delete()
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send('Member not found')

#@commands.check(check_if_its_me)
@client.command()
async def clears(ctx, *, amount = 1):
    await ctx.channel.purge(limit = amount)



@client.command(help = 'This returns latency')
async def ping(ctx):
    await ctx.send(f'{ round(client.latency * 1000) } ms!' )

#@commands.check(check_if_its_me)
@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *,reason = 'no reason given'):
    await ctx.send('lol join back')
    await ctx.send('https://discord.gg/CPdk369cFN')
    await member.kick(reason = reason)


@client.command(aliases = ['user'])
async def whois(ctx, member : discord.Member):
    embed = discord.Embed(title = member.name, description = member.mention, color = discord.Color.red() )
    embed.add_field(name = 'User ID', value = member.id, inline = False)
    await ctx.send(embed = embed)

@client.command(aliases = ['question'])
async def q(ctx, *, question):
    answers = ["It is certain.", "Without a doubt.", "Yes - definitely.",
    "As I see it, yes.", "Most likely.", "Yes.", "Signs point to yes.",
    "Ask again later.", "Better not tell you now. :wink:",
    "My reply is no.", "My sources say no.", "Very doubtful." ]
    await ctx.send(f'*`{ctx.author.name}`*: {question} \n*`Answer`*: { random.choice(answers) }')

@commands.check(check_if_its_exam)
@client.command()
async def clear(ctx, *, amount = 1):
    await ctx.channel.purge(limit = amount)




client.run('')












'''

@client.command(aliases = ['hello','hey'])
async def hi(ctx):
    hi = ['hi there.', 'hello', 'Whats up dude!', 'How ya doing!', 'heyy', 'Yo!', 'Hey buddy!']
    await ctx.send(f'{random.choice(hi)}..\n type "/help for more commands " ')
my id 351949188323475457 '''
