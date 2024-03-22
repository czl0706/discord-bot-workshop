from nextcord.ext import commands
from random import randint

from utils import in_specific_channel

channel_name = 'guess_number'

class GuessNum(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.answer = 0
        self.lower_bound, self.upper_bound = 0, 100
        self.started = False
        
    @in_specific_channel(channel_name)
    @commands.command()
    async def start_guessnum(self, ctx: commands.Context):
        """開始猜數字遊戲""" 
        if self.started:
            await ctx.reply("遊戲已經開始了")
            return
        self.lower_bound, self.upper_bound = 0, 100
        self.answer = randint(0, 100)
        self.started = True
        await ctx.reply("遊戲開始了，請輸入一個數字")
    
    @in_specific_channel(channel_name)
    @commands.command()
    async def guess(self, ctx: commands.Context, num: int):
        """猜數字""" 
        author = ctx.author.name
        
        if not self.started:
            await ctx.reply("遊戲還沒開始")
            return
        
        if num == self.answer:
            self.started = ...
            await ctx.reply(f"恭喜{author}猜對了!")
        elif num < self.answer:
            self.lower_bound = ...
            await ctx.reply(...)
        else:
            self.upper_bound = ...
            await ctx.reply(...)

def setup(bot: commands.Bot):
    bot.add_cog(GuessNum(bot))