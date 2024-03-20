import nextcord
from nextcord.ext import commands
import os

# 一開始bot開機需載入全部程式檔案
def load_extensions(bot: commands.Bot):
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")

# 定義一個檢查函數，用於檢查命令是否在特定頻道中使用
def in_specific_channel(channel_name: str):
    async def predicate(ctx):
        # 檢查命令的上下文中是否存在 channel 屬性
        if ctx.channel.name == channel_name:
            return True
        else:
            return False
    return commands.check(predicate)