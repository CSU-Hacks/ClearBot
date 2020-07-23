#main driver file for Clearbot

import discord

def get_token():
    token = ''
    with open('token.txt', 'r') as file:
        token += file.read()
    return token

client = discord.Client()

@client.event
async def on_ready():
    print('Client is online!')

client.run(get_token())