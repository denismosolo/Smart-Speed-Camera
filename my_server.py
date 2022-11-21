#server
import copy
import os
import random
import secrets
import threading
import time
import eventlet
import socketio
from termcolor import colored
from encrypt_decrypt_packet import decrypt_packet
from get_from_DB import get_key_from_DB
from GUI_DatiPatente import *
from Rete import get_plate

os.system('color')

global enc_packets
enc_packets = {}
d_nonce = {}
global arrived_photo
arrived_photo = False

#photo simulator
def take_photo():
    print(colored('\ngenerating photo...\n', 'red'))
    global arrived_photo
    t = random.randint(20,30)
    time.sleep(t)
    arrived_photo = True

#waiting for photo loop 
def waiting_loop():
    while True:
        global arrived_photo
        if arrived_photo:
            #flag reset
            arrived_photo = False
            #launch recognisation thread
            print(colored('\n...photo arrived\n', 'red'),colored('\nplate extraction started\n','yellow'))
            process_ph = threading.Thread(target=process_photo)
            process_ph.start()

            """UNCOMMENT TO RELUNCHING THE PHOTO SIMULATOR"""
            #photo = threading.Thread(target=take_photo)
            #photo.start()

            break
            

#photo and data processing
def process_photo():
    dict_targhe = {}
    #deep copy of the dict
    encrypted_packets = copy.deepcopy(enc_packets)
    time.sleep(3)
    print(colored(f"\ndecrypting packets...\n", 'yellow'))
    for secretID in encrypted_packets.keys():
        private_key = get_key_from_DB(secretID)
        targa,codice,result,message = decrypt_packet(private_key, encrypted_packets[secretID])
        if result:
            dict_targhe[targa] = codice
        else:
            print(colored(f"\nATTENZIONE:\nL'utente con secretID: {secretID} ha inviato i seguenti dati ma si è verificato un errore:\nTarga: {targa}\t Codice Patente: {codice}\nMessaggio di errore: {message}\n",'red'))
    print(colored(f"\ndictionary of client's data decrypted: \n", 'yellow'))
    [print(f"\t{key} : {value}") for key, value in dict_targhe.items()]
    print('\n\n')
    #chosing a photo between the plates arrived
    max = len(dict_targhe)-1
    photo_name = list(dict_targhe.items())[random.randint(0,max)][0]
    photo = f'{photo_name}.png'
    #extracting plate from photo
    plate = get_plate(photo)
    print(colored(f'\n\nPlate extracted from photo:', 'yellow'),f'\t{plate}\n')
    #GUI launching
    root=Tk()
    App=DataDisplayer(root, plate, dict_targhe[plate])
    time.sleep(3)
    root.mainloop()


def save_packet(sid, packet):
    secretID = packet.split('-')[0]
    if secretID in enc_packets.keys():
        pass
    elif len(enc_packets)>=10:
        #removes the oldest packet
        first_entry = list(enc_packets.items())[0][0]
        del enc_packets[first_entry]
        #inserts the new one
        enc_packets[secretID] = (packet.split('-')[1], d_nonce[sid])
        del d_nonce[sid]
    else:
        enc_packets[secretID] = (packet.split('-')[1], d_nonce[sid])
        del d_nonce[sid]

sio = socketio.Server()
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    print(colored(f'\nconnect {sid}]', 'green'))

@sio.on('requesting nonce')
def send_nonce(sid):
    nonce = secrets.token_hex(16) + '_' + str(int(time.time()))  #timestamp --> seconds since the epoch
    d_nonce[sid] = nonce
    sio.emit('nonce', nonce ,room=sid)
    print(colored(f'nonce sent to {sid}: \t{nonce}\n', 'yellow'))
    
@sio.event
def packet(sid, data):
    print(colored(f'message from {sid} is:', 'yellow'), f'  {data}')
    save_packet(sid, data)
    return True

@sio.event
def disconnect(sid):
    print(colored(f'disconnect {sid}\n', 'green'))

if __name__ == '__main__':
    loop = threading.Thread(target=waiting_loop)
    loop.start()
    photo = threading.Thread(target=take_photo)
    photo.start()
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app, log_output=False)

