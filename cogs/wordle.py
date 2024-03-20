from nextcord.ext import commands
import random

from utils import in_specific_channel

channel_name = 'wordle'

class Wordle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.answer = ''
        self.started = False
        
        with open('./assets/wordlist.txt', 'r', encoding='utf-8') as f:
            self.words = f.readlines()
            
    def start(self):
        self.answer = random.choice(self.words)
        self.answer = self.answer.strip()
        self.started = True
        print(f'答案是 {self.answer}')
        
    @in_specific_channel(channel_name)
    @commands.command()
    async def start_wordle(self, ctx: commands.Context):
        """開始Wordle遊戲""" 
        if self.started:
            await ctx.reply("遊戲已經開始了")
            return

        self.start()
        await ctx.reply('遊戲開始了')
    
    @in_specific_channel(channel_name)
    @commands.command()
    async def stop_wordle(self, ctx: commands.Context):
        """停止Wordle遊戲""" 
        if not self.started:
            await ctx.reply("遊戲還沒開始")
            return
        self.started = False
        await ctx.reply("遊戲停止了")
    
    @in_specific_channel(channel_name)
    @commands.command()
    async def wordle(self, ctx: commands.Context, uesr_input: str):
        """猜字""" 
        if not self.started:
            await ctx.reply("遊戲還沒開始")
            return
        
        if len(uesr_input) != len(self.answer):
            await ctx.reply(f"請輸入{len(self.answer)}個字")
            return
        
        result = ''
        for i in range(len(self.answer)):
            if self.answer[i] == uesr_input[i]:
                result += '🟩 '
            elif uesr_input[i] in self.answer:
                result += '🟨 '
            else:
                result += '⬛ '
                
        await ctx.reply(result)
        if result == '🟩 ' * len(self.answer):
            self.started = False
            await ctx.reply(f"恭喜{ctx.author.name}猜對了!")
            
            self.start()
            await ctx.send('遊戲開始了')

def setup(bot: commands.Bot):
    bot.add_cog(Wordle(bot))