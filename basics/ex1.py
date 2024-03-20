'''
dotenv, nextcord bot, decorator
'''
import nextcord

from dotenv import load_dotenv
import os

# client是跟nextcord連接，intents是要求機器人的權限
intents = nextcord.Intents.default()
intents.message_content = True
client = nextcord.Client(intents = intents)

# 調用event函式庫
@client.event
# 當機器人完成啟動
async def on_ready():
    print(f"目前登入身份: {client.user}")

@client.event
# 當頻道有新訊息
async def on_message(message):
    # author = message.author
    # content = message.content
    author, content = message.author, message.content
    
    print(f'Message from {author}: {content}')
    # 排除機器人本身的訊息，避免無限循環
    if author.name == client.user.name:
        return
    # 新訊息包含Hello，回覆Hello, world!
    if content.startswith("Hello"):
        await message.channel.send("Hello, world!")

load_dotenv(override=True)
API_KEY = os.getenv('DISCORD_API_KEY')
client.run(API_KEY)