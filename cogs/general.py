import nextcord
from nextcord.ext import commands
from utils import in_specific_channel

channel_name = 'general'

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # 範例指令: Hello
    @in_specific_channel(channel_name)
    @commands.command()
    async def Hello(self, ctx: commands.Context):
        # 加上docstring，可以在help指令中看到
        """對使用者回覆Hello""" 
        author = ctx.author.name
        # await ctx.send(f"Hello, {author}!")
        await ctx.reply(f"Hello, {author}!")

    # add
    ...
    
    # time
    ...
        
def setup(bot: commands.Bot):
    bot.add_cog(General(bot))