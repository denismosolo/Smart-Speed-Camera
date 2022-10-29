import psycopg2 as pg
from configDBconn import config


def get_data(ID_Patente):

    conn = None

    try:
        params=config()
        conn = pg.connect(**params)
        cur = conn.cursor()
    
        cur.execute('SELECT * FROM DatiPatenti WHERE Codice = %s', (ID_Patente,))

        row=cur.fetchone()
        
        cur.close()
    
    except (Exception, pg.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:            
            conn.close()
    
    return row

def get_key_from_DB(secretID):

    conn = None

    try:
        params=config()
        conn = pg.connect(**params)
        cur = conn.cursor()
    
        cur.execute('SELECT ChiavePrivata, N FROM DatiPatenti WHERE secretID = %s', (secretID,))

        row=cur.fetchone()
        
        cur.close()
    
    except (Exception, pg.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:            
            conn.close()

    d = int(row[0])
    n = int(row[1])
    
    return (d,n)

#data=get_key('WM562WT1FM')
#print (data)