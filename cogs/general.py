import nextcord
from nextcord.ext import commands
from utils import in_specific_channel

import random
import json

channel_name = 'general'

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # 讀入卡片資料
        with open('./assets/cats.json', 'r', encoding='utf-8') as f:
            self.cats = json.load(f)
        
    @in_specific_channel(channel_name)
    @commands.command()
    async def Hello(self, ctx: commands.Context):
        # 加上docstring，可以在help指令中看到
        """對使用者回覆Hello""" 
        author = ctx.author.name
        # await ctx.send(f"Hello, {author}!")
        await ctx.reply(f"Hello, {author}!")

    @in_specific_channel(channel_name)
    @commands.command()
    async def add(self, ctx: commands.Context, left: int, right: int):
        """Adds two numbers together."""
        await ctx.send(left + right)
    
    @in_specific_channel(channel_name)
    @commands.command()
    async def cat(self, ctx: commands.Context):
        # 隨機選一張照片
        cat = random.choice(self.cats)
        
        # 取得卡片標題和圖片連結
        tags = cat['tags']
        _id = cat['_id']
        
        link = 'https://cataas.com/cat/' + _id + '.jpeg'
        tag = random.choice(tags)
        
        await ctx.send(tag)
        await ctx.send(link)
        
def setup(bot: commands.Bot):
    bot.add_cog(General(bot))