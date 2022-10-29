from GUI_DatiPatente import *
import threading
import time
from Rete import get_plate

l_targa = ['EX539MT','EZ841TX','FB911NT','FK789EP','FP858MS','FS332VE','FT889TT','FX796HL','FX923HL','FY154KA']
l_codice_patente = ['UD1234567A','UD2345678B','UD3456789C','UD4567890D','UD5678901E','UD6789012F','UD7890123G','UD8901234H','UD9012345I','UD0123456J']


i=0

#for i in range (0,10) :
root=Tk()
App=DataDisplayer(root, l_targa[i], l_codice_patente[i])
root.mainloop()







#key = RSA.generate(2048)
#print(f"Public key:  (n={key.publickey().n}, e={key.publickey().e})")
#print('\n')
#print(f"Private key:  (n={key.n}, d={key.e})")

#cipher_rsa = PKCS1_OAEP.new(key.publickey().export_key())

#print(cipher_rsa)

#print(key.publickey().export_key())
#print(key.export_key())

"""
pr_key = '-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAuy1aYc/HzABF8OtopPI90YIYZz+IMZQhAWb4BLbWtoClFAhi\n+t94kc735TOz/UNf2I/ciSd9pjQfNyFARfcRQicAtarhrdA1yrc3yEf76pUfTP6e\ndrwdKbpFW5NHqSyltWy14wOlN8omDP/E7uDoRrLCpSTj5t/cU1PMAAgfiHyL5MPE\n1ceCJSk8UAV5TSnTIq8NwCxN7z/ANYNVNjY1nyWxzGEDiLoQ957Fl9JLfgih+9nH\nGJsE5fe3qOhpuTps3K34gjRj8LtQmLbBLkYT8HRUn1BcI0w3PS5coXyXMT7QFC2y\nix+/PT+87ibRUvjClVS7mezBINSk8r7R8rpB7wIDAQABAoIBAAJH0q6XaAFJzZBa\nZeuAkhU/5wk3AnNMMTzBour3yVTu61P7qC0TVPY91dJil2JSFFRgqFi5dPP19Z1n\n188ibADo1b7g5qAGBenC4ribe+vHRlrbTVX4A8jy3o53lGtwwlIcEXlDHZu46E7H\nPQCGF/5ohiuZ7/brqlUPk9A6SRwSFwz5vuS5XHY37CPKx9CVVgKCIwsw8+ZjGATE\noNu1a8Q9jgwrUE0Vigl1xrlgQFn6kTAAnY5gZCVDGzuhjul6UoiLbMJ1LDM4rbCP\n8yVwWbGjxnK4UmgPAF6DNpPDy2j9sq09VnN39bCgan5nkbsfYJ9LU72pIDNWv9LS\nsSzco1UCgYEAx8KKBwpODxDq8SPW2y9raUPH0lwLNV5u0nEUCGztEwa2WRAtzADv\n5uumVZE+v/eoi/CPbX+lECCMTyfPUtSzj+4YLrQGfuEfjpm7qxuAdR2DZaurA6vF\nyJadZqh1j8xFiJFP5bRICoMdUm3PM24z/hw3NZat5rjzeDL/gvf2lmUCgYEA79/t\nKOKi6GTAV8R+QLRgxKaXOa7UmnXjO7e5UXy7mQF9M1AztRQamKeFmnTe+UHK9AnA\nJvHxx/+HJEzoLxYlE3oPW+B5qpXRpbS3iGdAXjndMDITl4DaIdy4r8SmeMuxFx7V\nkE7GqcyI+EO6epDljPQ+DaGBQxfn2vj4NzzeN8MCgYB6A2uHjVXMggrfK4Lq8nXr\nIAmHhc0a1gle5M7VrqLIAkuS7vzqJJBkPf+lOEhZvQ3oHBGfUl4iEZ9iIfDSqTTc\nbxO6Qx/Mk/lQgrpMc0ntPw+pJEgav+rY8JZHxBG6uYynNArXRVzTfu6EEKqEwYVk\naxuV0el6ifG8s3m6J3couQKBgQCBjtukGozMoiY1AV8Diak+bY/+SsxvxL5/saK5\nPXqBkIlT3rye0AXxb4G8w+TukbeRiXasUj85u2z9kUBStk4+L8393Mc5+INsUahT\nVxkwC2bJMjLcwG6QnYtu+/LCCZpTl4bX04R/j4ZnOQWOT5Z8RCsD57hOSaoj3hcK\nlqibSwKBgFUVyRGdzBONnYfEI8Hzwmb+YCHqq/eaLcSbd9nFZo0+fA2AJ/Ds/hC3\nYF2SZD3AMWh0XKKNJFpq4g1mvjp5cwdVvlb+Tx6Ys/UUapTlj0c+63tQNIdUu5Fr\nFNLqyI9uhCZ9PqXPqUd7slKRHCn5p5Tx5j8AL4rZ4StBuXqjNpFq\n-----END RSA PRIVATE KEY-----'

pu_key = '-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuy1aYc/HzABF8OtopPI9\n0YIYZz+IMZQhAWb4BLbWtoClFAhi+t94kc735TOz/UNf2I/ciSd9pjQfNyFARfcR\nQicAtarhrdA1yrc3yEf76pUfTP6edrwdKbpFW5NHqSyltWy14wOlN8omDP/E7uDo\nRrLCpSTj5t/cU1PMAAgfiHyL5MPE1ceCJSk8UAV5TSnTIq8NwCxN7z/ANYNVNjY1\nnyWxzGEDiLoQ957Fl9JLfgih+9nHGJsE5fe3qOhpuTps3K34gjRj8LtQmLbBLkYT\n8HRUn1BcI0w3PS5coXyXMT7QFC2yix+/PT+87ibRUvjClVS7mezBINSk8r7R8rpB\n7wIDAQAB\n-----END PUBLIC KEY-----'

private_key=RSA.import_key(pr_key)

public_key=RSA.import_key(pu_key)

message = 'AA123BB-UD1234567A'.encode('utf-8')

cipher_rsa = PKCS1_OAEP.new(message)
enc_packet = cipher_rsa.encrypt(public_key)

cipher_rsa = PKCS1_OAEP.new(private_key)
dec_mex = cipher_rsa.decrypt(enc_packet)

print(dec_mex)

"""


"""
from Rete import get_plate

l_targa = ['HR26BC5514','889VSM','172TMJ','BCG986','BMW','CRAIG','G526JHD','LR33TEE','P3RVP','SKIPGAS']
l_codice_patente = ['UD1234567A','UD2345678B','UD3456789C','UD4567890D','UD5678901E','UD6789012F','UD7890123G','UD8901234H','UD9012345I','UD0123456J']

targa = get_plate(f'{l_targa[1]}.png')
print(targa)

from RSA import *
import math
from Crypto.Util import number


def generate_keys():
    rsa=RSA()

    p = number.getPrime(1024)
    q = number.getPrime(1024)
    #fargli generare due primi casuali da 1024bit
    #rsa.generateKeys(17055899557196527525682810191339089909014331959812898993437334555169285087976951946809555356817674844913188193949144165887100694620944167618997411049745043243260854998720061941490491091205087788373487296637817044103762239946752241631032791287021875863785226376406279424552454153388492970310795447866569138481,
    #            171994050316145327367864378293770397343246561147593187377005295591120640129800725892235968688434055779668692095961697434700708550594137135605048681344218643671046905252163983827396726536078773766353616572531688390937410451433665914394068509329532352022301339189851111636176939179510955519440490431177444857017)
    rsa.generateKeys(p,q)

    p_key = [str(x) for x in list(rsa.getPublicKey())]
    public_key = tuple(p_key)
    private_key = rsa.getPrivateKey()

    return ([public_key, private_key])

print(generate_keys())
"""





#root.geometry('300x200')
"""
from tkinter import *
from tkinter import font
root=Tk()
l1=Text(root)
l1.pack()
Button(root,text='get label font',command=lambda: print(font.nametofont(l1['font']).configure()["family"])).pack()
root.mainloop()
"""
"""
from tkinter import *  
from PIL import ImageTk,Image
from get_from_DB import get_data
import io

data=get_data('UD1234567A')
file=open('Vuota.png', "rb")
foto=file.read()

root = Tk()
frame=Frame(root) 
canvas = Canvas(frame, width = 800, height = 800, background='black')  
canvas.pack()  
#img = Image.open("Vuota.png")
#img = ImageTk.PhotoImage(data=data[9], format='png')
#img = ImageTk.PhotoImage(data=foto, format='png')
img = Image.open(io.BytesIO(data[9]))
resized_image= img.resize((30,50), Image.ANTIALIAS) 
new_img=ImageTk.PhotoImage(resized_image)
canvas.create_image(1, 1, anchor=NW, image=new_img) 
frame.pack()
root.mainloop() 
"""


"""

from tkinter import *
from PIL import Image,ImageTk

#Create an instance of tkinter frame
win = Tk()

#Set the geometry of tkinter frame
win.geometry("750x270")

#Create a canvas
canvas= Canvas(win, width= 600, height= 400)
canvas.pack()

#Load an image in the script
img= (Image.open("Vuota.png"))

#Resize the Image using resize method
resized_image= img.resize((300,205), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
canvas.create_image(10,10, anchor=NW, image=new_image)

win.mainloop()
"""