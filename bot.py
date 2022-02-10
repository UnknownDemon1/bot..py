import discord
from discord.ext import commands

prefix='='



intents=discord.Intents.default()
intents = discord.Intents(messages=True, guilds=True)
client = commands.Bot(command_prefix=prefix, intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="Testing bot"))
    print('Bot is online')

#command
@client.command()
async def Hello(ctx):
    await ctx.send('**Hello, How are you today? (1. Good, 2. Ok, 3. Sad)** to answer my question please write this command `=A1` or `=A2` or `=A3`')

@client.command()
async def A1(ctx):
    await ctx.send('**Thats really good to know hope you have a great day**')

@client.command()
async def A2(ctx):
    await ctx.send('**Why are you not happy, Wanna be happy? watch funny videos - https://youtu.be/fAlvKlweR2U **')

@client.command()
async def A3(ctx):
    await ctx.send('**Why are you Sad how about talk to some friends or play something fun** *another command :/* `=no_friends`')

@client.command()
async def no_friends(ctx):
    await ctx.send('**If you dont have friends then I can be your AI friend**')

client.run('TOKEN')

