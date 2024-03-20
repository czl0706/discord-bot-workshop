'''
dotenv, nextcord bot, decorator
'''
import nextcord
from nextcord.ext import commands

from dotenv import load_dotenv
import os

# bot是跟nextcord連接，intents是要求機器人的權限
intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = '!', intents = intents)

# decoracor
@bot.event
# 當機器人完成啟動
async def on_ready():
    print(f"目前登入身份: {bot.user}")

@bot.event
# 當頻道有新訊息
async def on_message(message):
    # author = message.author
    # content = message.content
    author, content = message.author, message.content
    
    print(f'Message from {author}: {content}')
    # 排除機器人本身的訊息，避免無限循環
    if author.name == bot.user.name:
        return
    # 新訊息包含hello，回覆你好！
    if "hello" in content.lower():
        await message.channel.send("你好！")

load_dotenv(override=True)
API_KEY = os.getenv('DISCORD_API_KEY')
bot.run(API_KEY)