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
        ...:
            self.decks = ...
        
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
    async def bonk(self, ctx: commands.Context):
        # 隨機選一張卡片
        card = ...
        
        # 取得卡片標題和圖片連結
        title = ...
        image_link = ...
        
        await ctx.send(f'{title}')
        await ctx.send(f'{image_link}')
        
def setup(bot: commands.Bot):
    bot.add_cog(General(bot))