#handles the basic interepretation of leaving server commands

import discord, psycopg2, time #external libraries
import leaving_server.server_leave_postgres as server_leave_postgres #internal libraries

async def leaving_server_handler(server):
    server_id = server.id
    await server_leave_postgres.remove_server_entry(server_id)