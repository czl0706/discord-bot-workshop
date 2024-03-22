from nextcord.ext import commands
from utils import in_specific_channel
import os 
import json
import datetime

API_KEY = os.getenv('CWA_API_KEY')

import requests

channel_name = 'general'

class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def forecast(self, ctx: commands.Context):
        """新竹市天氣預報"""
        url = f'https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-D0047-053?Authorization={API_KEY}&locationName=%E6%9D%B1%E5%8D%80&limit=10&format=JSON&elementName=T'
        json_data = requests.get(url).json()

        # 不一定要照著做
        
        # 取得資料
        temp_data = ...

        # 格式化時間
        processed_data = [(
            ... , ...
            ) for data in temp_data]

        # 過濾時間，只取未來的時間
        filtered_data = [(
            ... , ...
            ) for data in processed_data if data[0] > datetime.datetime.now()]
        
        # 只取前五筆
        filtered_data = filtered_data[:5]

        # 回覆天氣預報
        await ctx.reply('\n'.join([f'{data[0]}: **{data[1]}°C**' for data in filtered_data]))
        
def setup(bot: commands.Bot):
    bot.add_cog(Weather(bot))