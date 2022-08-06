import os
os.system("cls && color 4 && title SPEMER")
print("Enter the token | Введите токен бота")
token = input("Token:  ")
import random
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "$", help_command=None, self_bot = False)
guild  = client.get_guild(id)

@client.event
async def on_ready():
  print("""
                     ___________ ________  ___ ___________ 
 Developed          /  ___| ___ \  ___|  \/  ||  ___| ___ \
 by                 \ `--.| |_/ / |__ | .  . || |__ | |_/ /
 Know                `--. \  __/|  __|| |\/| ||  __||    / 
                    /\__/ / |   | |___| |  | || |___| |\ \ 
                    \____/\_|   \____/\_|  |_/\____/\_| \_|""")
  while True:
    a = 0
@client.command()
async def start(ctx, text):
  while True:
     ctx.send("Spemer #" + random.randint(9999, 10000) + text)


client.run(token)