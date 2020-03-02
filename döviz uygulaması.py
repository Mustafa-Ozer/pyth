import sys
from PyQt5 import QtWidgets
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import sqlite3

try:
    def dovizcek():
        url = "https://www.doviz.com/"
        response = requests.get(url)
        html_ic = response.content
        soup = BeautifulSoup(html_ic,"html.parser")
        doviz_ismi = soup.find_all("span",{"class":"name"})
        deger = soup.find_all("span",{"class":"value"})
        a=list()
        for isim,deger in zip(doviz_ismi,deger):
            if(isim.text == "DOLAR"):
                usd = (isim.text,deger.text)
                a.append(usd)
            elif(isim.text=="EURO"):
                euro = (isim.text,deger.text)
                a.append(euro)
            elif (isim.text == "GRAM ALTIN"):
                gram = (isim.text, deger.text)
                a.append(gram)
            elif (isim.text == "STERLİN"):
                sterlin = (isim.text, deger.text)
                a.append(sterlin)
                break
        return a
    su_an = datetime.now()
    usd = list()
    euro = list()
    gram = list()
    sterlin = list()
    a=0
    for i,j in dovizcek():
        if(a==0):
            usd.append(i)
            usd.append(j)
            a=1
        elif(a==1):
            euro.append(i)
            euro.append(j)
            a=2
        elif(a == 2):
            gram.append(i)
            gram.append(j)
            a = 3
        elif(a == 3):
            sterlin.append(i)
            sterlin.append(j)
            a = 4
    a=0
    for i in usd:
        if(a==0):
           isim=i
           a=1
        else:
           deger=i
    a=0
    for i in euro:
        if(a==0):
          isim2=i
          a=1
        else:
          deger2=i
    a=0
    for i in gram:
        if(a==0):
            isim3=i
            a=1
        else:
            deger3=i
    a=0
    for i in sterlin:
        if(a==0):
            isim4=i
            a=1
        else:
            deger4=i
    con = sqlite3.connect("doviz.db")
    cursor = con.cursor()
    def tablo_olustur():
        cursor.execute("CREATE TABLE IF NOT EXISTS doviz(Tarih TEXT,Saat TEXT,Dolar INT,Euro INT,Gram_Altın INT,Sterlin INT)")
        con.commit()
    def verileri_kaydet(tarih,saat,dolar,euro,gram,sterlin):
        cursor.execute("INSERT INTO doviz Values(?,?,?,?,?,?)",(tarih,saat,dolar,euro,gram,sterlin))
        con.commit()
    def veri_al(tarih):
        cursor.execute("Select * From doviz where Tarih = ?",(tarih,))
        liste = cursor.fetchall()
        for i in liste:
            t=0
            print("********************************")
            for x in i:
                if(t==0):
                    print("Tarih : {}".format(x))
                elif(t==1):
                    print("Saat : {}".format(x))
                elif(t==2):
                    print("Dolar : {} TL".format(x))
                elif(t==3):
                    print("Euro : {} TL".format(x))
                elif(t==4):
                    print("Gram Altın : {} TL".format(x))
                elif(t==5):
                    print("Sterlin : {} TL".format(x))
                t+=1
            print("********************************")
    saat = ("{} : {} : {}".format(su_an.hour,su_an.minute,su_an.second))
    tarih=("{} / {} / {}".format(su_an.day,su_an.month,su_an.year))
    tablo_olustur()
    verileri_kaydet(tarih,saat,deger2,deger3,deger,deger4)
    try:
        x = input("Tarih gir(G / A / YYYY) : ")
        veri_al(x)
    except:
        pass
except:
    a="nc"

def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Doviz")
    buton = QtWidgets.QPushButton(pencere)
    buton.setText("Hesapla")
    buton2 = QtWidgets.QPushButton(pencere)
    buton2.setText("Kapat")
    h_box = QtWidgets.QHBoxLayout()
    v_box = QtWidgets.QVBoxLayout()
    etiket = QtWidgets.QLabel(pencere)
    etiket.setText("ANLIK DÖVİZ KURLARI")
    etiket.move(160,50)
    if(a!="nc"):
        etiket2=QtWidgets.QLabel(pencere)
        etiket2.setText("""
            SAAT {} : {} : {}\tTARIH {}/{}/{}\n
    SADECE BU SAAT VE TARIH ICIN GECERLIDIR\n   
        -------------------------------------------------
                          {} : {}
                
                          {} : {}
                
                          {} : {}
        
                          {} : {}
        -------------------------------------------------
            """.format(su_an.hour,su_an.minute,su_an.second,su_an.day,su_an.month,su_an.year,isim,deger,isim2,deger2,isim3,deger3,isim4,deger4))
        etiket2.move(80,120)
    else:
        etiket2 = QtWidgets.QLabel(pencere)
        etiket2.setText("BAGLANTI YOK")
        etiket2.move(200,150)
    birim = QtWidgets.QLabel(pencere)
    birim.setText("TL'ye Cevrilecek Para Birimi :")
    miktar = QtWidgets.QLabel(pencere)
    miktar.setText("Miktar :")
    yazi_alani = QtWidgets.QLineEdit()
    yazi_alani2 = QtWidgets.QLineEdit()
    v_box.addStretch()
    v_box.addWidget(etiket)
    v_box.addWidget(etiket2)
    v_box.addWidget(birim)
    v_box.addWidget(yazi_alani)
    v_box.addWidget(miktar)
    v_box.addWidget(yazi_alani2)
    v_box.addWidget(buton)
    v_box.addWidget(buton2)
    v_box.addStretch()
    h_box.addStretch()
    h_box.addLayout(v_box)
    h_box.addStretch()
    etp = QtWidgets.QLabel(pencere)
    v_box.addWidget(etp)
    def hesap():
        pbirim = yazi_alani.text()
        pbirim = pbirim.upper()
        try:
            pmiktar = float(yazi_alani2.text())
            if (pbirim == "DOLAR"):
                etp.setText("{} TL".format(pmiktar*float(deger2.replace(",","."))))
                v_box.addWidget(etp)
            elif (pbirim == "GRAM ALTIN"):
                etp.setText("{} TL".format(pmiktar*float(deger.replace(",","."))))
                v_box.addWidget(etp)

            elif (pbirim == "EURO"):
                etp.setText("{} TL".format(pmiktar*float(deger3.replace(",","."))))
                v_box.addWidget(etp)

            elif (pbirim == "STERLIN" or pbirim == "STERLİN"):
                etp.setText("{} TL".format(pmiktar*float(deger4.replace(",","."))))
                v_box.addWidget(etp)
            else:
                etp.setText("Lutfen Yukaridaki Para Birimlerinden Birini Giriniz.")

        except:
            etp.setText("Bir Hata Olustu!")
            v_box.addWidget(etp)

    def kapat():
        sys.exit(app.exec_())

    buton.clicked.connect(hesap)
    buton2.clicked.connect(kapat)
    pencere.setLayout(v_box)
    pencere.setLayout(h_box)
    pencere.setGeometry(430,150,320,250)
    pencere.show()
    sys.exit(app.exec_())

Pencere()
con.close()
