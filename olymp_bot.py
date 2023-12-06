import discord
import os
from dotenv import load_dotenv
import random
import fortnite_api

import constants

load_dotenv()
bot = discord.Bot()

api = fortnite_api.FortniteAPI(os.getenv('FN_STATS_API_TOKEN'))

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond(constants.hello_response)

@bot.slash_command(name = "answer", description = "What do you get if you multiply six by nine?")
async def answer(ctx):
    await ctx.respond("42")

@bot.slash_command(name = "fzitat", description = "Ein zufälliges falsch zugeordnetes Zitat bitte!")
async def fzitat(ctx):
    await ctx.respond(constants.wrong_citations[random.randint(0, len(constants.wrong_citations) - 1)])

@bot.slash_command(name = "soon", description = "When will it happen?")
async def hello(ctx):
    await ctx.respond(constants.soon_response)

@bot.slash_command(name = "stats", description = "Get the stats of a fortnite player")
async def stats(ctx, pname):
    await ctx.respond(api.stats.fetch_by_name(name = pname, image = fortnite_api.enums.StatsImageType.ALL).image_url)
bot.run(os.getenv('OLYMP_TOKEN'))
