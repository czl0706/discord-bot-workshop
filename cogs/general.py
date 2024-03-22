import nextcord
from nextcord.ext import commands
from utils import in_specific_channel
import time as t

channel_name = 'general'

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
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
        
    # @in_specific_channel(channel_name)
    # @commands.command()
    # async def time(self, ctx: commands.Context):
    #     """顯示時間"""
    #     time_now = t.strftime("%Y年%m月%d日 %H點%M分", t.localtime())
    #     await ctx.send(f'現在時間: {time_now}')
        
def setup(bot: commands.Bot):
    bot.add_cog(General(bot))