import discord
import os
from discord.ext import commands
from discord.ext.commands import Bot
import random
from decouple import config

#client = discord.Client(activity=discord.Game(name='my game'))

wrong_citations = ['„Frage nicht, was dein Land für dich tun kann, frage was du für dein Land tun kannst.“ - Kim Jong-il',
                    '„Willst du den Charakter eines Menschen erkennen, so gib ihm Macht.“ - Roland Koch',
                    '„Mister Gorbatschow, tear down this wall!“ - David Hasselhoff',
                    '„Dies ist mein Leib, der für euch hingegeben wird.“ - Gina Wild']

bot = commands.Bot(command_prefix = '>') #put your own prefix here
#new comment
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
async def antwort(ctx):
    await ctx.send("42!")

@bot.command()
async def soon(ctx):
    await ctx.send("\"Soon\" does not imply any particular date, time, decade, century, or millennia in the past, present, and certainly not the future. \"Soon\" shall make no contract or warranty between Cohhilition and the end user. \"Soon\" will arrive some day, CohhCarnage does guarantee that \"soon\" will be here before the end of time. Maybe. Do not make plans based on \"soon\" as CohhCarnage will not be liable for any misuse, use, or even casual glancing at \"soon.\"")

@bot.command()
async def ping(ctx):
    await ctx.send("pong!") #simple command so that when you type "!ping" the bot will respond with "pong!"

@bot.command()
async def wrong_citation(ctx):
    randNum = random.randrange(0, len(wrong_citations))
    await ctx.send(wrong_citations[randNum])

bot.run(config('OLYMP_TOKEN'))
