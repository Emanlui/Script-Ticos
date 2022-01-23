#!/usr/bin/python
from PIL import Image
import os
from shutil import copyfile
cont = 0
error_list = []

for root, dirs, files in os.walk("."):

    for file in files:
        imagen = root + "\\" + file
        try:
            date = Image.open(imagen)._getexif()[36867].split(":")[0]
            extension = imagen.split(".")[-1]
            
            copyfile(imagen, "C:\\Users\\Emanlui\\Desktop\\Desktop\\Fotos ordenadas\\"+ str(date) +"\\foto" + str(cont) + "."+extension)
            cont = cont + 1
        except Exception as e:
            if(str(e) not in  error_list):
                error_list.append(str(e))
            pass


print(error_list)
print("Done")
