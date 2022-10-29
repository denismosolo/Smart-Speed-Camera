#server
import eventlet
import socketio
from encrypt_decrypt_packet import generate_keys, decrypt_packet
import os
from termcolor import colored
import threading
import time
import random
from Rete import get_plate
from GUI_DatiPatente import *
from get_from_DB import get_key_from_DB
import secrets
import copy

os.system('color')

global enc_packets
enc_packets = {}
d_nonce = {}
global arrived_photo
arrived_photo = False

#photo simulator
def take_photo():
    print(colored('generating photo...', 'red'))
    global arrived_photo #devo dichiararla ogni volta che la devo modificare
    t = random.randint(25,30)
    time.sleep(t)
    arrived_photo = True

#waiting for photo loop 
def waiting_loop():
    while True:
        global arrived_photo
        if arrived_photo:
            #resetto il flag
            arrived_photo = False
            #eseguo thread di riconoscimento
            print(colored('foto arrivata', 'red'))
            process_ph = threading.Thread(target=process_photo)
            process_ph.start()
            break
            """SOLO AI FINI DELLA SIMULAZIONE"""
            #riavvio il thread di simulazione della foto
            #photo = threading.Thread(target=take_photo)
            #photo.start()
        #print("CONTINUO L'ATTESA")

def process_photo():
    #l_key_pck = []
    dict_targhe = {}
    #copio dizionari pacchetti e chiavi
    encrypted_packets = copy.deepcopy(enc_packets)
    for secretID in encrypted_packets.keys():
        private_key = get_key_from_DB(secretID)
        targa,codice,result,message = decrypt_packet(private_key, encrypted_packets[secretID])
        #print(f'Analizzo il pacchetto di:\t{secretID}')
        if result:
            dict_targhe[targa] = codice
        else:
            print(colored(f"ATTENZIONE:\nL'utente con secretID: {secretID} ha inviato i seguenti dati ma si è verificato un errore:\nTarga: {targa}\t Codice Patente: {codice}\nMessaggio di errore: {message}",'red'))
    print(colored(dict_targhe, 'yellow'))
    #scelgo una foto in base alle targhe disponibili
    max = len(dict_targhe)-1
    photo_name = list(dict_targhe.items())[random.randint(0,max)][0]
    photo = f'{photo_name}.png'
    #print(colored(photo, 'red'))
    #p=['HR26BC5514.png']
    #photo=p[0]#random.randint(0,1)]
    plate = get_plate(photo)
    print(colored(plate, 'yellow'))
    #targa=list(dict_targhe.items())[0][0]
    #scarico i dati dal server
    root=Tk()
    App=DataDisplayer(root, plate, dict_targhe[plate])
    root.mainloop()


#aggiungere la rimozione dei vecchi pacchetti
def save_packet(sid, packet):
    secretID = packet.split('-')[0]
    if secretID in enc_packets.keys():
        pass
    elif len(enc_packets)>=10:
        #rimuovi il primo pacchetto (il più vecchio) e la relativa chiave
        first_entry = list(enc_packets.items())[0][0]
        del enc_packets[first_entry]
        #inserisci il nuovo pacchetto
        enc_packets[secretID] = (packet.split('-')[1], d_nonce[sid])
        del d_nonce[sid]
    else:
        enc_packets[secretID] = (packet.split('-')[1], d_nonce[sid])
        del d_nonce[sid]

sio = socketio.Server()
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    print(colored(f'connect {sid}]', 'green'))

@sio.on('requesting nonce')
def send_nonce(sid):
    nonce = secrets.token_hex(16) + '_' + str(int(time.time()))  #timestamp --> seconds since the epoch, in caso sostituire con data/ora
    d_nonce[sid] = nonce
    sio.emit('nonce', nonce ,room=sid)
    print(colored(f'nonce sent to {sid}: \t{nonce}', 'yellow'))
    
@sio.event
def packet(sid, data):
    print(colored(f'message from {sid} is: \t{data}', 'yellow'))
    save_packet(sid, data)
    return True

@sio.event
def disconnect(sid):
    print(colored(f'disconnect {sid}', 'green'))

if __name__ == '__main__':
    loop = threading.Thread(target=waiting_loop)
    loop.start()
    photo = threading.Thread(target=take_photo)
    photo.start()
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)

