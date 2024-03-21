import nextcord
from nextcord.ext import commands
from utils import in_specific_channel

channel_name = 'general'

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @in_specific_channel(channel_name)
    @commands.command()
    async def Hello(self, ctx: commands.Context):
        ...

    # add
    ...
    
    # time
    ...
        
def setup(bot: commands.Bot):
    bot.add_cog(General(bot))