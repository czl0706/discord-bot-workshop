from nextcord.ext import commands
import nextcord
from utils import in_specific_channel

import requests
import json 

import random

with open('./assets/cards.json', 'r', encoding='utf-8') as f:
    decks = json.load(f)

channel_name = 'general'

class Dogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @in_specific_channel(channel_name)
    @commands.command()
    async def bonk(self, ctx: commands.Context):
        card = random.choice(decks)
        
        title = card['title']
        image_link = card['src']
        
        await ctx.send(f'{title}')
        await ctx.send(f'{image_link}')

    @in_specific_channel(channel_name)
    @commands.command()
    async def dog(self, ctx: commands.Context):
        response = requests.get('https://dog.ceo/api/breeds/image/random')
        image_link = response.json()['message']
        await ctx.send(image_link)
        
def setup(bot: commands.Bot):
    bot.add_cog(Dogs(bot))