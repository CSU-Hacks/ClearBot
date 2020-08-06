#main driver file for Clearbot

import discord, logging
from discord.ext import commands
import joining_server.server_join_postgres, joining_server.server_join_handler #internal libraries

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot = commands.Bot(command_prefix='!')

def get_token():
    token = ''
    with open('token.txt', 'r') as file:
        token += file.read()
    return token

@bot.event
async def on_ready():
    #await joining_server.server_join_handler.new_server_handler(725357725546053685, "Nickle's Server of Cake and Suffering", 475488656170156039)
    print('Ready!')

@bot.event
async def on_guild_join(server):
    await joining_server.server_join_handler.new_server_handler(server)
    

@bot.event
async def on_guild_remove(server):
    print(str(server.id))

@bot.command()
async def test(ctx, *args):
    print('it happens')
    await ctx.send(args)
"""
@bot.command()
async def other_test(ctx, *args):
    print('ruh roh')
    await ctx.send(args)
"""
bot.run(get_token())