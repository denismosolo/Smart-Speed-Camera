import os
import sys
import psycopg2 as pg
import argparse
from configDBconn import config

listNames = ['Marco','Maria','Mario','Luca','Giulia','Monica','Giacomo','Fabio','Luigi','Aldo']

def main(argv):
    parser = argparse.ArgumentParser()
    parser_action = parser.add_mutually_exclusive_group(required=True)
    parser_action.add_argument("--store", action='store_const', const=True, help="Load an image from the named file and save it in the DB")
    parser_action.add_argument("--fetch", action='store_const',const=True, help="Fetch an image from the DB and store it in the named file, overwriting it if it exists. Takes the database file identifier as an argument.")

    args = parser.parse_args(argv[1:])

    params=config()
    conn = pg.connect(**params)
    cur = conn.cursor()

    
    if args.store:
        
        for name in listNames:
            f = open(f'foto_patente\{name}.png', 'rb')

            filedata = f.read()
            cur.execute("UPDATE DatiPatenti SET Foto = %s WHERE Nome = %s", (filedata,name))
            
            f.close()
            conn.commit()
            print(f"Stored {name} into DB record")

    elif args.fetch is not None:
        # Fetches the file from the DB into memory then writes it out.
        for name in listNames:
            f = open(f'{name}.png','wb')
            cur.execute("SELECT Foto FROM DatiPatenti WHERE Nome = %s", (name,))
            file_data = cur.fetchone()

            f.write(file_data[0])
            f.close()
            print(f"Fetched {name} into file {name}.png")

    conn.close()

if __name__ == '__main__':
    main(sys.argv)