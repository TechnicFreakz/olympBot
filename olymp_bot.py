import discord
import os
from discord.ext import commands
from discord.ext.commands import Bot
import random

#client = discord.Client(activity=discord.Game(name='my game'))

wrong_citations = ['„Frage nicht, was dein Land für dich tun kann, frage was du für dein Land tun kannst.“ - Kim Jong-il',
                    '„Willst du den Charakter eines Menschen erkennen, so gib ihm Macht.“ - Roland Koch',
                    '„Mister Gorbatschow, tear down this wall!“ - David Hasselhoff',
                    '„Dies ist mein Leib, der für euch hingegeben wird.“ - Gina Wild']

bot = commands.Bot(command_prefix = '$') #put your own prefix here

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    await ctx.send("pong!") #simple command so that when you type "!ping" the bot will respond with "pong!"

@bot.command()
async def wrong_citation(ctx):
    randNum = random.randrange(0, len(wrong_citations))
    await ctx.send(wrong_citations[randNum])

bot.run(os.getenv('OLYMP_TOKEN'))
