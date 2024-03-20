import nextcord
from nextcord.ext import commands
from utils import in_specific_channel
import requests

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
        
    def dog(self, ):
        response = requests.get('https://dog.ceo/api/breeds/image/random')
        image_link = response.json()['message']
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