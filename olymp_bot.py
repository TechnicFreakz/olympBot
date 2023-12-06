import discord
import os
from dotenv import load_dotenv

load_dotenv()
bot = discord.Bot()


wrong_citations = ['"Frage nicht, was dein Land für dich tun kann, frage was du für dein Land tun kannst." Kim Jong-il',]

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")

@bot.slash_command(name = "answer", description = "What do you get if you multiply six by nine?")
async def answer(ctx):
    await ctx.respond("42")

bot.run(os.getenv('OLYMP_TOKEN'))
