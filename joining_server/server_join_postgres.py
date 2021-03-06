#handles postgres function relating to the bot joining a new server

import psycopg2 #external libraries
from configparser import ConfigParser

async def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section not found in the file')
    return db

async def new_server_added(server_id, name, owner_id):
    conn = None
    try:
        params = await config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('SET search_path TO public;')
        cur.callproc('new_server_added', [server_id, str(name), owner_id])
        conn.commit()
        conn.close()
        return True
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return False
    finally:
        if conn is not None:
            conn.close()

async def new_server_add_users(user_list, server_id):
    conn = None
    try:
        params = await config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('SET search_path TO public;')
        cur.callproc('new_server_user_list', [user_list, server_id])
        conn.commit()
        conn.close()
        return True
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return False
    finally:
        if conn is not None:
            conn.close()