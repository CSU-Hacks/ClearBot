#handles postgres function relating to the bot leaving a new server

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

async def remove_server_entry(server_id):
    conn = None
    try:
        params = await config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('SET search_path TO public;')
        cur.callproc('removed_from_server', [server_id])
        conn.commit()
        conn.close()
        return True
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return False
    finally:
        if conn is not None:
            conn.close()