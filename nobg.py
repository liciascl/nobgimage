# Requires "requests" to be installed (see python-requests.org)
import sys
import subprocess as cmd
from PIL import Image
import os, shutil
import requests

#try:
    #pega quantas imagens precisa tirar o fundo

dir = os.getcwd()
dir = dir + "/fotos_com_fundo/"
print (dir)
for index, file in enumerate(os.listdir(dir)):
    #renomeia as imagens com fundo
    antiga=dir+file
    nova_com_fundo=dir+"image"+str(index)+".png"
    os.rename(antiga,nova_com_fundo)
    print("{} renomeada para image{}.png".format(file,index))

    print("tirando o fundo da imagem")
    response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file': open(nova_com_fundo, 'rb')},
    data={'size': 'auto'},
    headers={'X-Api-Key': 'Z6oCZ7L15ervntLoxLWZJAaq'},
)
    if response.status_code == requests.codes.ok:
        filename = '/home/borg/Desktop/no-bg/fotos_sem_fundo/SemFundo_{}.png'.format(index)
        with open(filename, 'wb') as out:
            out.write(response.content)
            print("Fundo Retirado com sucesso")
            print("deixando com 800px")
            basewidth = 800
            img = Image.open(filename)
            wpercent = (basewidth/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
            img = img.resize((basewidth,hsize), Image.ANTIALIAS)
            img.save(filename) 













