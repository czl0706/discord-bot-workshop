'''
指令, type hint, docstring(!help), library name conflict
https://docs.python.org/zh-tw/3.10/library/datetime.html#strftime-and-strptime-format-codes
'''
import nextcord
from nextcord.ext import commands

from dotenv import load_dotenv
import os

import time as t

# client是跟nextcord連接，intents是要求機器人的權限
intents = nextcord.Intents.default()
intents.message_content = True
# command_prefix是前綴符號，可以自由選擇($, #, &...)
bot = commands.Bot(command_prefix = '!', intents = intents)

@bot.event
# 當機器人完成啟動
async def on_ready():
    print(f"目前登入身份: {bot.user}")

@bot.command()
async def Hello(ctx: commands.Context):
    # 加上docstring，可以在help指令中看到
    """對使用者回覆Hello""" 
    author = ctx.author.name
    # await ctx.send(f"Hello, {author}!")
    await ctx.reply(f"Hello, {author}!")

@bot.command()
async def add(ctx: commands.Context, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)
    
@bot.command()
async def time(ctx: commands.Context):
    """顯示時間"""
    time_now = t.strftime("%Y年%m月%d日 %H點%M分", t.localtime())
    await ctx.send(f'現在時間: {time_now}')
    
load_dotenv(override=True)
API_KEY = os.getenv('DISCORD_API_KEY')
bot.run(API_KEY)