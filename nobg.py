# Requires "requests" to be installed (see python-requests.org)
import sys
import subprocess as cmd
from PIL import Image
import os, shutil
import requests

try:
    print("Puxando novos arquivos")   
    cp = cmd.run("git add .", check=True, shell=True)


except:
    print (cp)

dir = os.getcwd()
dir = dir + "/fotos_com_fundo/"
print (dir)
for index, file in enumerate(os.listdir(dir)):
    #renomeia as imagens com fundo
    antiga=dir+file
    nova=dir+"image0"+str(index)
    if antiga == nova:
        print ("As fotos ja foram tratadas")
        exit
    
    else:
        if antiga == "teste.md":
            exit
        os.rename(antiga,nova)
        print("{} renomeada para image{}".format(file,index))
        try:
            print("tirando o fundo da imagem")
            response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': open(nova, 'rb')},
            data={'size': 'auto'},
            headers={'X-Api-Key': 'Z6oCZ7L15ervntLoxLWZJAaq'},
        )
            print("status", response.status_code)
        except:
            print("erro", response.status_code)
        if response.status_code == requests.codes.ok:
            filename = '/home/borg/Desktop/nobgimage/fotos_sem_fundo/SemFundo_{}.png'.format(index)
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

        try:
            cp = cmd.run("rm -rf /home/borg/Desktop/nobgimage/fotos_com_fundo/image0*", check=True, shell=True)
            cp = cmd.run("git add .", check=True, shell=True)
            print("Imagem sem bg subindo")
            message = "Imagem sem bg subindo"
            cp = cmd.run(f"git commit -m '{message}'", check=True, shell=True)
            cp = cmd.run("git push -u origin master -f", check=True, shell=True)
            print (cp)
        except:
            print(cp)









