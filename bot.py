from discord.ext import commands
import discord
import settings
from scrape.py import easy_question

def run():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        print(f"Logged in as: {bot.user} (ID: {bot.user.id})")

    @bot.command()
    async def ping(ctx):
        await ctx.send()

    bot.run(settings.Discord_API_Secret, root_logger=True)

if __name__ == "__main__":
    run()