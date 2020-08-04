#Handles the process of the bot being joined to a new server

import discord, psycopg2, time #external libraries
import joining_server.server_join_postgres as server_join_postgres#internal library

async def new_server_handler(server_id, server_name, owner_id):
    """server_id = server.id
    owner_id = server.owner_id
    server_name = server.name"""
    await server_join_postgres.new_server_added(server_id, str(server_name), owner_id)
    return
    