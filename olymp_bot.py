import discord
import os
from dotenv import load_dotenv
import random
from .constants import *

load_dotenv()
bot = discord.Bot()


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond(hello_response)

@bot.slash_command(name = "answer", description = "What do you get if you multiply six by nine?")
async def answer(ctx):
    await ctx.respond("42")

@bot.slash_command(name = "fzitat", description = "Ein zufälliges falsch zugeordnetes Zitat bitte!")
async def fzitat(ctx):
    await ctx.respond(wrong_citations[random.randint(0, len(wrong_citations) - 1)])
    
@bot.slash_command(name = "soon", description = "When will it happen?")
async def hello(ctx):
    await ctx.respond(soon_response)

bot.run(os.getenv('OLYMP_TOKEN'))
