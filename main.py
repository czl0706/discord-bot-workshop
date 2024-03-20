import nextcord
from nextcord.ext import commands

from dotenv import load_dotenv
import os

from utils import load_extensions

# bot是跟discord連接，intents是要求機器人的權限
intents = nextcord.Intents.default()
intents.message_content = True
# # intents.members = True
# intents = discord.Intents.all()

# command_prefix是前綴符號，可以自由選擇($, #, &...)
bot = commands.Bot(command_prefix = '!', intents = intents)

@bot.event
async def on_ready():
    print(f"目前登入身份: {bot.user}")
    
@bot.event
async def on_member_join(member):
    guild, name = member.guild, member.name
    channel = nextcord.utils.get(guild.channels, name="general")
    
    await channel.send(f"哈嘍, {name}!")


load_dotenv(override=True)
API_KEY = os.getenv('DISCORD_API_KEY')
        
load_extensions(bot)
bot.run(API_KEY)