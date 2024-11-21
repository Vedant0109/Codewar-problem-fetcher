
from scraper import easy_question
from discord import Intents
from discord.ext import commands
from discord.ext import tasks

from selenium import webdriver

import settings
import asyncio

class Bot(commands.Bot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.driver = webdriver.Chrome()

    async def setup_hook(self):
        await self.scrape.start()
    
    @tasks.loop(hours=1)
    async def scrape(self):
        easy_question(self.driver)

    @scrape.before_loop
    async def before_loop(self):
        await self.wait_until_ready()

async def main():
    intents = Intents.all()
    bot = Bot(command_prefix='!', intents=intents)

    await bot.start(settings.Discord_API_Secret)

if __name__ == "__main__":
    asyncio.run(main())