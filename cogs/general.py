import nextcord
from nextcord.ext import commands
from utils import in_specific_channel

import requests
import random
import json

channel_name = 'general'

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # 讀入卡片資料
        with open('./assets/cards.json', 'r', encoding='utf-8') as f:
            self.decks = json.load(f)
        
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
        
    def dog(self, ):
        json_data = requests.get('https://dog.ceo/api/breeds/image/random').json()
        image_link = json_data['message']
        return image_link
        
    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        author, content = message.author, message.content
        
        # check if the message is from channel_name
        if message.channel.name != channel_name:
            return
        
        if author.name == self.bot.user.name:
            return
        
        if any(x in content for x in ('狗', 'dog')):
            message = await message.reply(self.dog())
        
def setup(bot: commands.Bot):
    bot.add_cog(General(bot))