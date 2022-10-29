import math
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import re
import secrets

def generate_keys():

    key = RSA.generate(2048)
    public_key = (key.e, key.n)
    private_key = (key.d, key.n)

    return ((public_key, private_key))


def create_encrypted_packet(targa, codice_patente, e, n, id, nonce):
    s = targa + '-' + codice_patente + '-' + nonce

    # Hash function calculation
    f_hash = SHA256.new(data=str.encode(s)).hexdigest()

    # Append the hash function
    st = s + '/' + f_hash

    # Convert the string in utf-8 then in integer to pass the value to the encryptor
    packet = int.from_bytes(st.encode('utf-8'), byteorder='big', signed=False)

    encrypted = pow(packet, int(e), int(n))

    enc_packet = id + '-' + str(encrypted)

    return enc_packet


def decrypt_packet(key, pck):    #due tuple: key=(d,n) pck=(packet,nonce)
    
    d = key[0]
    n = key[1]
    encrypted = int(pck[0])
    nonce = pck[1]

    decrypted = pow(encrypted, d, n)

    st = (decrypted).to_bytes(math.ceil((decrypted).bit_length() / 8), byteorder = 'big', signed=False).decode('utf-8')

    s = st.split('/')   #[0] message - [1] hash function

    f_hash = SHA256.new(data = str.encode(s[0])).hexdigest()

    # Hash function comparison
    if secrets.compare_digest(f_hash, s[1]):
        l_string = s[0].split('-')  #[0] targa - [1] codice patente - [2] nonce

        # Nonce comparison
        if secrets.compare_digest(nonce, l_string[2]):
            #print(f'nonce inviato:\t{nonce}\nnonce ricevuto:\t{l_string[2]}')

            # Correct format verification
            pattern_t = re.compile(r"^([A-Z]{2}[0-9]{3}[A-Z]{2})?$")
            if pattern_t.match(l_string[0]):
                pattern_cp = re.compile(r"^([A-Z]{2}[0-9]{7}[A-Z])?$")
                if pattern_cp.match(l_string[1]):
                    result = True
                    message = 'All good'
                else:
                    result = False
                    message = 'Invalid licence ID'
            else:
                result = False
                message = 'Invalid plate'
        else:
            result = False
            message = 'Nonce verification failed'
            print(f'nonce inviato:\t{nonce}\nnonce ricevuto:\t{l_string[2]}')
    else:
        result = False
        message = 'Hash verification failed'
    
    return l_string[0], l_string[1], result, message

    

