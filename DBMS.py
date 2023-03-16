import psycopg2 as db

database_name = 'DBPost'
user = 'postgres'
password = 'admin'

conn = db.connect(database= database_name, user = user, password = password, host = 'localhost')

cursor = conn.cursor()

    
def commit():
    return conn.commit()

# commit()


def create_table(cur):


    cur.execute("""CREATE TABLE IF NOT EXISTS Songs(
    artist_id varchar(200),
    serial_id varchar(200),
    song varchar(200),
    title varchar(500)
    )""")
    
    return conn.commit()

def songs_insert(cur, values : list):
    cur.execute("INSERT INTO Songs VALUES (%s, %s, %s, %s)", values)
    return conn.commit()

def songs_double_check():
    cursor.execute('select artist_id from songs limit 1')
    dataset = cursor.fetchone()
    try:
        if dataset[0] == 'AR002UA1187B9A637D':
            return True
        else:
            return False
    except:
        return False


create_table(cursor)




conn.close
