import nextcord
from nextcord import ButtonStyle, Interaction
from nextcord.ui import Button, View

from nextcord.ext import commands
from typing import List

from utils import in_specific_channel

from random import shuffle, choice

channel_name = 'bingo'

class BingoBoardButton(Button['BingoBoard']):
    def __init__(self, update_player, x: int, y: int, enabled: bool, label: str):
        super().__init__(style=ButtonStyle.secondary if label != '0' else ButtonStyle.success, 
                         label=label, 
                         row=y)
        self.x = x
        self.y = y
        self.update_player = update_player
        button_enabled = (label != '0') and enabled
        self.disabled = not button_enabled

    async def callback(self, interaction: Interaction):
        assert self.view is not None
        view: BingoBoard = self.view
        num = view.board[self.y][self.x]
        if num == 0:
            return

        player_id = interaction.user.id

        view.board[self.y][self.x] = 0

        # 更新所有玩家的状态
        await interaction.response.edit_message(content='更新中...')
        await self.update_player(player_id, num)

class BingoBoard(View):
    def __init__(self, board, update_player, enabled: bool = True):
        super().__init__()
        self.board = board
        for x in range(5):
            for y in range(5):
                self.add_item(BingoBoardButton(update_player, 
                                               x, 
                                               y, 
                                               enabled,
                                               str(board[y][x])))
                
class Bingo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.started = False
        self.player_states = {}
        
    def create_bingo_board(self):
        board_list = list(range(1, 25 + 1))
        shuffle(board_list)
        board = [board_list[5 * i: 5 * i + 5] for i in range(0, 5)]
        return board
        
    @in_specific_channel(channel_name)
    @commands.command()
    async def start_bingo(self, ctx: commands.Context):
        """開始Bingo遊戲""" 
        if self.started:
            await ctx.reply("遊戲已經開始了")
            return
        if len(self.player_states) < 2:
            await ctx.reply("至少需要兩個玩家才能開始遊戲")
            return
        
        self.started = True
        self.send_message = ctx.send
        await ctx.reply("遊戲開始了")
        await self.update_player(choice(list(self.player_states.keys())), 0)
    
    @in_specific_channel(channel_name)
    @commands.command()
    async def join_bingo(self, ctx: commands.Context):
        """加入Bingo遊戲""" 
        if self.started:
            await ctx.reply("遊戲已經開始了")
            return

        board = self.create_bingo_board()
        
        await ctx.reply(f"{ctx.author.name}加入了遊戲")
        message = await ctx.author.send('這是你的棋盤', view=BingoBoard(board, self.update_player, False))
        self.player_states[ctx.author.id] = {'board': board, 'message': message, 'name': ctx.author.name}
        
    async def update_player(self, id, num):
        # find the next player
        player_ids = list(self.player_states.keys())
        index = player_ids.index(id)
        next_id = player_ids[(index + 1) % len(player_ids)]
        next_name = self.player_states[next_id]['name']
        winner = ''
        
        for player_id, player_state in self.player_states.items():
            player_state['board'] = [[0 if cell == num else cell for cell in row] for row in player_state['board']]
            bingo = self.check_bingo(player_state['board'])
            
            if bingo:
                winner = player_state['name']
                self.started = False
                break
            
            if player_id == next_id:
                view = BingoBoard(player_state['board'], self.update_player, player_id == next_id)
                await player_state['message'].edit(view = view, content = f'輪到你了')
            else:
                view = BingoBoard(player_state['board'], self.update_player, player_id == next_id)
                await player_state['message'].edit(view = view, content = f'輪到{next_name}了')
        
        if self.started == False:
            await self.send_message(f'遊戲結束, {winner}獲勝了')
            for player_id, player_state in self.player_states.items():
                view = BingoBoard(player_state['board'], self.update_player, False)
                await player_state['message'].edit(view = view, content = f'遊戲結束, {winner}獲勝了')
    
    def check_bingo(self, board):
        for i in range(5):
            if all([cell == 0 for cell in board[i]]):
                return True
            if all([board[j][i] == 0 for j in range(5)]):
                return True
        if all([board[i][i] == 0 for i in range(5)]):
            return True
        if all([board[i][4 - i] == 0 for i in range(5)]):
            return True
        return False

def setup(bot: commands.Bot):
    bot.add_cog(Bingo(bot))