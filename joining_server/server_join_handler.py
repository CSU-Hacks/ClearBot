#Handles the process of the bot being joined to a new server

import discord, psycopg2, time #external libraries
import joining_server.server_join_postgres as server_join_postgres #internal library

async def new_server_handler(server):
    server_id = server.id
    owner_id = server.owner_id
    server_name = server.name
    user_list = server.members
    user_id_list = []
    for user in user_list:
        user_id_list.append(user.id)
    await server_join_postgres.new_server_added(server_id, str(server_name), owner_id)
    await server_join_postgres.new_server_add_users(user_id_list, server_id)
    return
    