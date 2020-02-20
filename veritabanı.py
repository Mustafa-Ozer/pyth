import sqlite3
import time

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_Sayısı INT)")
    con.commit()
   
def veri_ekle2(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("INSERT INTO kitaplık Values(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()

def veri_al():
    cursor.execute("Select * From kitaplık"),
    liste = cursor.fetchall()
    print("Kitaplık Bilgileri...........")
    time.sleep(1)
    for i in liste:
        print(i)
        time.sleep(0.5)

def veri_al2():
    cursor.execute("Select İsim,Yazar From kitaplık")
    liste = cursor.fetchall()
    print("Kitaplık Bilgileri...........")
    time.sleep(1)
    for i in liste:
        print(i)
        time.sleep(0.5)

def veri_al3(isim):
    cursor.execute("Select * From kitaplık where İsim = ?",(isim,))
    liste = cursor.fetchall()
    for i in liste:
        time.sleep(0.5)
        print(i)

def veri_al4(yazar):
    cursor.execute("Select * From kitaplık where Yazar = ?",(yazar,))
    liste = cursor.fetchall()
    for i in liste:
        time.sleep(0.5)
        print(i)

def veri_al5(yayınevi):
    cursor.execute("Select * From kitaplık where Yayınevi = ?",(yayınevi,))
    liste = cursor.fetchall()
    for i in liste:
        time.sleep(0.5)
        print(i)
def kitap_upd(eski,yeni):
    cursor.execute("Update kitaplık set İsim = ? where İsim = ?",(yeni,eski))
    con.commit()
    
def veri_sil(kitap):
    cursor.execute("Delete From kitaplık where İsim = ?",(kitap,))
    con.commit()
tablo_olustur()

print("""
************************************************
İŞLEMLER

1.Kitap Ekle
2.Bütün Kitapları Göster
3.Kitap Bilgilerini Göster
4.Yazar'ın Eserlerini Göster
5.Yayınevinin Yayınladığı Kitapları Göster
6.Kitap Adını Değiştir
7.Kitap Sil
8.Çık
************************************************
""")
while True:
    islem=int(input("İşlem Seç(1,2...): "))
    
    if(islem==1):    
        isim = input("Kitap Adı :")
        yazar = input("Yazar:")
        yayınevi = input("Yayınevi:")
        sayfa_sayısı = input("Sayfa Sayısı:")
        veri_ekle2(isim,yazar,yayınevi,sayfa_sayısı)
    elif(islem==2):
        veri_al()
    elif(islem==3):
        b=input("Kitap Adı:")
        veri_al3(b)
    elif(islem==4):
        b=input("Yazar Adı:")
        veri_al4(b)
    elif(islem==5):
        b=input("Yayınevi :")
        veri_al5(b)
    elif(islem==6):
        b=input("Eski Kitap Adı:")
        c=input("Yeni Kitap Adı:")
        kitap_upd(b,c)
    elif(islem==7):
        b=input("Silinecek Kitap Adı:")
        veri_sil(b)
    elif(islem==8):
        break

    
con.close()
