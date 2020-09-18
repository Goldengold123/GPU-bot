import discord

from discord.ext import commands
from discord import Embed
from dotenv import load_dotenv
from credentials import TOKEN, PREFIX

load_dotenv()

bot = commands.Bot(PREFIX)


# Connecting to Discord

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


# Tic Tac Toe

@bot.command(name='tictactoe', help='Tic Tac Toe for 2 players.')
async def tictactoe(ctx):
    def createEmbed(gameNum, description, colour):
        myEmbed = discord.Embed(
            title='Tic Tac Toe - G'+str(gameNum),
            description=description,
            colour=colour,
        )
        return myEmbed
    checkPlayers = createEmbed(1, 'Tic Tac Toe for 2 players.', 0x55ACEE)
    checkPlayers.set_footer(text='Player 1 react with ❌, Player 2 react with ⭕.')
    sent = await ctx.send(embed=checkPlayers)
    await sent.add_reaction('❌')
    await sent.add_reaction('⭕')
    def checkReaction(reaction, user):
        if str(reaction.emoji) == '❌':
            user1 = user
        if str(reaction.emoji) == '⭕':
            user2 = user

    letters = {
        'A': '🇦',
        'B': '🇧',
        'C': '🇨',
        'D': '🇩',
        'E': '🇪',
        'F': '🇫',
        'G': '🇬',
        'H': '🇭',
        'I': '🇮'
    }
    filled = []
    possibleMoves = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

    def drawBoard():
        horizontal = '🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦'
        mainLine = '⬛⬛⬛🟦⬛⬛⬛🟦⬛⬛⬛'
        top = '⬛{0}⬛🟦⬛{1}⬛🟦⬛{2}⬛'.format(letters['A'], letters['B'], letters['C'])
        middle = '⬛{0}⬛🟦⬛{1}⬛🟦⬛{2}⬛'.format(letters['D'], letters['E'], letters['F'])
        bottom = '⬛{0}⬛🟦⬛{1}⬛🟦⬛{2}⬛'.format(letters['G'], letters['H'], letters['I'])
        board = '{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n{7}\n{8}\n{9}\n{10}'.format(mainLine, top, mainLine, horizontal,
                                                                                mainLine, middle, mainLine, horizontal,
                                                                                mainLine, bottom, mainLine)
        return board

    def win(myBoard, piece):
        if myBoard['A'] == myBoard['B'] == myBoard['C'] == piece:
            return True
        elif myBoard['D'] == myBoard['E'] == myBoard['F'] == piece:
            return True
        elif myBoard['G'] == myBoard['H'] == myBoard['I'] == piece:
            return True
        elif myBoard['A'] == myBoard['D'] == myBoard['G'] == piece:
            return True
        elif myBoard['B'] == myBoard['E'] == myBoard['H'] == piece:
            return True
        elif myBoard['C'] == myBoard['F'] == myBoard['I'] == piece:
            return True
        elif myBoard['A'] == myBoard['E'] == myBoard['I'] == piece:
            return True
        elif myBoard['C'] == myBoard['E'] == myBoard['G'] == piece:
            return True
        else:
            return False

    def draw(myBoard, myFilled):
        return (not (win(myBoard, '❌'))) and (not (win(myBoard, '⭕'))) and len(myFilled) == 9

    while not (draw(letters, filled)) and not (win(letters, '❌')) and not (win(letters, '⭕')):

    '''
    while not (draw(letters, filled)) and not (win(letters, '❌')) and not (win(letters, '⭕')):

        await ctx.send(drawBoard() + '\n' + 'Player 1, send the letter of where you would like to go.')

        def check1(m):
            return (m.author == user1 and
                    m.channel == channel1 and
                    not (m.content.upper() in filled) and
                    m.content.upper() in possibleMoves)

        move1 = await bot.wait_for('message', check=check1)
        letters[move1.content.upper()] = '❌'
        filled.append(move1.content.upper())
        if win(letters, '❌'):
            await ctx.send('Congrats! Player 1 has won!' + '\n' + drawBoard())
            break
        if draw(letters, filled):
            await ctx.send('The 2 players have drew! HAHA, that means I win!' + '\n' + drawBoard())
            break
        await ctx.send(drawBoard() + '\n' + 'Player 2, send the letter of where you would like to go.')

        def check2(m):
            return (m.author == user2 and
                    m.channel == channel2 and
                    not (m.content.upper() in filled) and
                    m.content.upper() in possibleMoves)

        move2 = await bot.wait_for('message', check=check2)
        letters[move2.content.upper()] = '⭕'
        filled.append(move2.content.upper())
        if win(letters, '⭕'):
            await ctx.send('Congrats! Player 2 has won!' + '\n' + drawBoard())
            break
    '''

bot.run(TOKEN)
