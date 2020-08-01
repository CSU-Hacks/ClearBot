#Handles the process of the bot being joined to a new server

import discord, psycopg2, time #external libraries

async def new_server_handler(server):
    server_id = server.id
    owner_id = server.owner_id
    server_name = server.name