from encrypt_decrypt_packet import generate_keys
import random
from string import ascii_uppercase
import psycopg2 as pg
from configDBconn import config

l_keys = []
listNames = ['Marco','Maria','Mario','Luca','Giulia','Monica','Giacomo','Fabio','Luigi','Aldo']

f=open('n.txt', 'a')

params=config()
conn = pg.connect(**params)
cur = conn.cursor()

for i in range (0,10):
    keys = generate_keys()
    f.write(f'coppia{i}: \n e = {str(keys[0][0])} \n d = {str(keys[1][0])} \n n = {str(keys[0][1])} \n')
    cur.execute("UPDATE DatiPatenti SET ChiavePrivata = %s WHERE Nome = %s", (int(keys[1][0]),listNames[i]))
    cur.execute("UPDATE DatiPatenti SET N = %s WHERE Nome = %s", (int(keys[1][1]),listNames[i]))
    conn.commit()
    print(f"Stored {listNames[i]} into DB record")
conn.close()
f.close()



def generate_secretid():
    spec = [
        *[ascii_uppercase] * 2,
        range(1,9),range(1,9),range(1,9),
        *[ascii_uppercase] * 2,
        range(1, 9), *[ascii_uppercase]*2,
    ]
    for i in range(0,10):
        print(''.join(str(random.choice(pool)) for pool in spec),'\n')



listNames = ['Marco','Maria','Mario','Luca','Giulia','Monica','Giacomo','Fabio','Luigi','Aldo']

def store(l_keys):

    params=config()
    conn = pg.connect(**params)
    cur = conn.cursor()

        
    for i in range(0,10):
  
        cur.execute("UPDATE DatiPatenti SET ChiavePrivata = %d WHERE Nome = %s", (l_keys[i][1][0],listNames[i]))
        cur.execute("UPDATE DatiPatenti SET N = %d WHERE Nome = %s", (l_keys[i][1][1],listNames[i]))
        conn.commit()
        print(f"Stored {listNames[i]} into DB record")

    conn.close()

