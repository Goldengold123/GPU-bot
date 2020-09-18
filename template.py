import discord

from discord.ext import commands
from dotenv import load_dotenv
from credentials import TOKEN, PREFIX

load_dotenv()

bot = commands.Bot(PREFIX)


# Connecting to Discord

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


bot(TOKEN)