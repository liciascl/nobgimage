# Requires "requests" to be installed (see python-requests.org)
import requests
import subprocess as cmd
from PIL import Image
import sys



try:
    down = ""
   # down = cmd.run("wget https://raw.githubusercontent.com/liciascl/nobgimage/master/ImagemComFundo.jpg", check=True, shell=True)
    print("Download Realizado com Sucesso")

    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open('/home/borg/Desktop/no-bg/ImagemComFundo.jpg', 'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': 'Z6oCZ7L15ervntLoxLWZJAaq'},
    )
    if response.status_code == requests.codes.ok:
        with open('ImagemSemFundo.png', 'wb') as out:
            out.write(response.content)
            print("Fundo Retirado com sucesso")
            filename = 'ImagemSemFundo.png'
            basewidth = 800
            img = Image.open(filename)
            wpercent = (basewidth/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
            img = img.resize((basewidth,hsize), Image.ANTIALIAS)
            img.save(filename) 
            print("deixando com 800px")



            cp = cmd.run("git add .", check=True, shell=True)
            print("Imagem sem bg subindo")
            message = "Imagem sem bg subindo"
            cp = cmd.run(f"git commit -m '{message}'", check=True, shell=True)
            cp = cmd.run("git push -u origin master -f", check=True, shell=True)
            
    else:
        print("Error:", response.status_code, response.text)


except:
    print("Deu errooo")







