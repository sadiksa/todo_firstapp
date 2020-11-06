import sqlite3
import time


db = sqlite3.connect("toDo.db")
imlec = db.cursor()
imlec.execute("CREATE TABLE IF NOT EXISTS notlar (notsayisi, notismi, notum, edittarihi)")



while True:
    print("""
            ToDo App (by Sadik first time)
            [1] Notları göster
            [2] Not ekle
            [3] ToDo'yu kapat
    
    """)
    secim = input("Seçimin?")
    if secim == "1":
        notisimlerisorgu = imlec.execute("SELECT notismi FROM notlar")
        notisimleri = imlec.fetchall()
        sayac = 1
        for i in notisimleri:
            print(sayac, ") ",[i][0][0])
            sayac +=1
        print("Çıkmak için q ' ya basınız")
        sorgu2 = input("Seçiminiz?")

        if sorgu2 == "q" or sorgu2 == "Q":
            print("Ana menüye dönülüyor...")
        else:
            secim2 = int(sorgu2)
            notgostersorgu = imlec.execute("SELECT * FROM notlar WHERE notsayisi={}".format(secim2))
            notgoster = imlec.fetchall()
            print(notgoster[0][0], ".not")
            print("Notun ismi: ", notgoster[0][1])
            print("Notun düzenlenme tarihi: ", notgoster[0][3])
            print("*"*20)
            print(notgoster[0][2])
            print("*" * 20)
            print("""
            [1] Notu sil
            [2] Ana menüye dön
            """)
            secim3 = input("Seçiminiz?")
            if secim3 == "1":
                imlec.execute("DELETE FROM notlar WHERE notsayisi={}".format(notgoster[0][0]))
            elif secim3 == "2":
                print("Ana menüye dönülüyor...")
            else:
                print("Anlaşılamadı. Ana menüye dönülüyor...")


    elif secim == "2":
        imlec.execute("SELECT notsayisi FROM notlar")
        cikti = imlec.fetchall()
        notsayisi = int(cikti[-1][0])+1
        eklenecek_not_ismi= input("Notun ismi?")
        eklenecek_not= input("Notunuz?")
        zaman = time.localtime()
        zaman_cikti =str(zaman.tm_hour)+ ":"+ str(zaman.tm_min)+ " - "+ str(zaman.tm_mday)+ "/"+ str(zaman.tm_mon)+ "/"+ str(zaman.tm_year)
        girdi = (notsayisi, eklenecek_not_ismi, eklenecek_not, zaman_cikti)
        imlec.execute("INSERT INTO notlar VALUES (?, ?, ?, ?)", girdi)
        db.commit()
    elif secim == "3":
        db.close()
        quit()
    else:
        print("Seçim algılanamadı.")



db.close()
