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
        response = requests.get(f'https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-D0047-053?Authorization={API_KEY}&locationName=%E6%9D%B1%E5%8D%80&limit=10&format=JSON&elementName=T')
        data = json.loads(response.text)
        temp_data = data['records']['locations'][0]['location'][0]['weatherElement'][0]['time']

        processed_data = [(
            datetime.datetime.strptime(data['dataTime'], '%Y-%m-%d %H:%M:%S'),
            int(data['elementValue'][0]['value'])
            ) for data in temp_data]

        filtered_data = [(
            data[0].strftime('%d號 %H點'), data[1]
            ) for data in processed_data if data[0] > datetime.datetime.now()]
        
        filtered_data = filtered_data[:5]

        await ctx.reply('\n'.join([f'{data[0]}: **{data[1]}°C**' for data in filtered_data]))
        
def setup(bot: commands.Bot):
    bot.add_cog(Weather(bot))