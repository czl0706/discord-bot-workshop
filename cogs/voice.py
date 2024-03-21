from nextcord.ext import commands
from utils import in_specific_channel

import nextcord 
from nextcord import FFmpegPCMAudio
from gtts import gTTS
from datetime import datetime

from pytube import YouTube, Playlist

channel_name = 'general'

class Voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @in_specific_channel(channel_name)
    @commands.command()
    async def join_voice(self, ctx, *, channel: nextcord.VoiceChannel):
        """Joins a voice channel"""

        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await channel.connect()
    
    @in_specific_channel(channel_name)
    @commands.command()
    async def stop_voice(self, ctx):
        """Stops and disconnects the bot from voice"""
        await ctx.voice_client.disconnect()
        
    @in_specific_channel(channel_name)
    @commands.command()
    async def time(self, ctx: commands.Context):
        """回覆現在時間""" 
        vc = ctx.voice_client
        
        if vc is not None:
            tts = gTTS(text=datetime.now().strftime('現在時間是%H點%M分'), lang='zh-tw')
            tts.save('./assets/time.mp3')
            
            if vc.is_playing():
                vc.stop()
            
            vc.play(FFmpegPCMAudio('./assets/time.mp3'))
        else:
            await ctx.reply(datetime.now().strftime('現在時間是: %H:%M'))
            
    @commands.command()
    async def play_music(self, ctx, *, video_id):
        vc = ctx.voice_client

        if vc is not None:
            try:
                YouTube(f'https://youtu.be/{video_id}').streams \
                    .filter(only_audio=True).first() \
                    .download(filename='./assets/music.mp3')
            except:
                await ctx.reply('URL錯誤')
                return
            
            if vc.is_playing():
                vc.stop()
            
            vc.play(FFmpegPCMAudio('./assets/music.mp3'))
        else:
            await ctx.reply('請先加入語音頻道')
        
def setup(bot: commands.Bot):
    bot.add_cog(Voice(bot))