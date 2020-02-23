import sqlite3
import time

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_Sayısı INT,Stok INT)")
    con.commit()
   
def veri_ekle(isim,yazar,yayınevi,sayfa_sayısı,stok):
    cursor.execute("INSERT INTO kitaplık Values(?,?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı,stok))
    con.commit()

def veri_al():
    cursor.execute("Select * From kitaplık"),
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
        return
    print("Böyle Bir Kitap Yok.")
def veri_al4(kitap):
    cursor.execute("Select Stok From kitaplık where İsim = ?",(kitap,))
    liste = cursor.fetchall()
    for i in liste:
        for x in i:
            print(x)
            return
    print("Stokta Böyle Bir Kitap Yok.")

def kitap_upd(eski,yeni):
    cursor.execute("Update kitaplık set İsim = ? where İsim = ?",(yeni,eski))
    con.commit()
    
def veri_sil(kitap):
    cursor.execute("Delete From kitaplık where İsim = ?",(kitap,))
    con.commit()
def kitap_sat(kitap,k):
    try:
        cursor.execute("Select Stok From kitaplık where İsim = ?",(kitap,))
        liste = cursor.fetchall()
        for i in liste:
            for x in i:
                a=x
        if(a-k>=0):
            cursor.execute("Update kitaplık set Stok = ? where Stok = ?",(a-k,a))
            con.commit()
            if(a-k==0):
                print("{} tükendi.".format(kitap))
        else:
            print("Stokta o kadar kitap yok.")
    except:
        print("Kitap Bilgileri Sistemde Kayıtlı Değildir.\nÖnce Kitap Bilgilerini Eklemeniz Gerekmektedir.")
    
def gelen_kitap(kitap,k):
    try:
        cursor.execute("Select Stok From kitaplık where İsim = ?",(kitap,))
        liste = cursor.fetchall()
        for i in liste:
            for x in i:
                a=x
        cursor.execute("Update kitaplık set Stok = ? where Stok = ?",(a+k,a))
        con.commit()
    except:
        print("Kitap Bilgileri Sistemde Kayıtlı Değildir.\nÖnce Kitap Bilgilerini Eklemeniz Gerekmektedir.")
    
    
tablo_olustur()

print("""
************************************************
İŞLEMLER

1.Kitap Ekle
2.Bütün Kitapları Göster
3.Kitap Bilgilerini Göster
4.Kitaptan kaç tane kaldığını göster
5.Kitap Adını Değiştir
6.Kitap Sil
7.Kitap Sat
8.Gelen Kitapları Veri Tabanına Ekle
9.Çık
************************************************
""")
while True:
    try:
        islem=int(input("İşlem Seç(1,2...): "))
    except:
        print("Hatalı Giriş Yaptınız.")
        continue
    if(islem==1):    
        isim = input("Kitap Adı: ")
        yazar = input("Yazar: ")
        yayınevi = input("Yayınevi: ")
        sayfa_sayısı = input("Sayfa Sayısı: ")
        stok =input("Stok: ")
        veri_ekle(isim,yazar,yayınevi,sayfa_sayısı,stok)
    elif(islem==2):
        veri_al()
    elif(islem==3):
        b=input("Kitap Adı: ")
        veri_al3(b)
    elif(islem==4):
        b=input("Kitap Adı: ")
        veri_al4(b)
    elif(islem==5):
        b=input("Eski Kitap Adı: ")
        c=input("Yeni Kitap Adı: ")
        kitap_upd(b,c)
    elif(islem==6):
        b=input("Silinecek Kitap Adı: ")
        veri_sil(b)
    elif(islem==7):
        b=input("Satılan Kitap Adı: ")
        try:
            c=int(input("Kaç Tane Satıldı: "))
        except:
            print("Hatalı Giriş Yaptınız.")
            continue
        kitap_sat(b,c)    
    elif(islem==8):
        b=input("Gelen Kitap Adı: ")
        try:
            c=int(input("Kaç Tane Geldi: "))
        except:
            print("Hatalı Giriş Yaptınız.")
            continue
        gelen_kitap(b,c)    
    elif(islem==9):
        break
    else:
        print("Hatalı Giriş Yaptınız.")
    
    

    
con.close()
