
from scraper import easy_question
from discord import Intents
from discord.ext import commands
from discord.ext import tasks

from selenium import webdriver

import asyncio

from os import getenv

from dotenv import load_dotenv

class Cog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        description = easy_question(self.bot.driver)
        await ctx.reply(description)

class Bot(commands.Bot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.driver = webdriver.Chrome()

    async def setup_hook(self):
        # await self.scrape.start()
        await self.add_cog(Cog(self))
    
    # @tasks.loop(hours=1)
    # async def scrape(self):
    #     easy_question(self.driver)

    # @scrape.before_loop
    # async def before_loop(self):
    #     await self.wait_until_ready()

async def main():
    intents = Intents.default()
    intents.message_content=True

    bot = Bot(command_prefix='!', intents=intents)

    load_dotenv()

    await bot.start(getenv('BOT_TOKEN'))

if __name__ == "__main__":
    asyncio.run(main())