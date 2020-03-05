import sys
from PyQt5 import QtWidgets
from datetime import datetime
from bs4 import BeautifulSoup
import requests

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
        etiket3=QtWidgets.QLabel(pencere)
        gram = QtWidgets.QRadioButton(pencere)
        usd = QtWidgets.QRadioButton(pencere)
        euro = QtWidgets.QRadioButton(pencere)
        ster = QtWidgets.QRadioButton(pencere)
        etiket2.setText("""
            SAAT {} : {} : {}\tTARIH {}/{}/{}\n
    SADECE BU SAAT VE TARIH ICIN GECERLIDIR\n   
        -------------------------------------------------""".format(su_an.hour,su_an.minute,su_an.second,su_an.day,su_an.month,su_an.year))
        gram.setText("     {} : {}    ".format(isim,deger))
                        
        usd.setText("     {} : {}    ".format(isim2,deger2))
                
        euro.setText("     {} : {}    ".format(isim3,deger3))
        
        ster.setText("     {} : {}    ".format(isim4,deger4))
        etiket3.setText("       -------------------------------------------------")
        etiket2.move(80,120)
    else:
        etiket2 = QtWidgets.QLabel(pencere)
        etiket2.setText("BAGLANTI YOK")
        etiket2.move(200,150)
    miktar = QtWidgets.QLabel(pencere)
    miktar.setText("Miktar :")
    yazi_alani2 = QtWidgets.QLineEdit()
    v_box.addStretch()
    v_box.addWidget(etiket)
    v_box.addWidget(etiket2)
    v_box.addWidget(gram)
    v_box.addWidget(usd)
    v_box.addWidget(euro)
    v_box.addWidget(ster)
    v_box.addWidget(etiket3)
    v_box.addWidget(miktar)
    v_box.addWidget(yazi_alani2)
    v_box.addWidget(buton)
    v_box.addWidget(buton2)
    v_box.addStretch()
    h_box.addStretch()
    h_box.addLayout(v_box)
    h_box.addStretch()
    etp = QtWidgets.QLabel(pencere)
    def hesap(gram,usd,euro,ster):
        try:
            pmiktar = float(yazi_alani2.text())
            if usd:
                etp.setText("{} TL".format(pmiktar*float(deger2.replace(",","."))))
                v_box.addWidget(etp)
            if gram:
                etp.setText("{} TL".format(pmiktar*float(deger.replace(",","."))))
                v_box.addWidget(etp)

            if euro:
                etp.setText("{} TL".format(pmiktar*float(deger3.replace(",","."))))
                v_box.addWidget(etp)

            if ster:
                etp.setText("{} TL".format(pmiktar*float(deger4.replace(",","."))))
                v_box.addWidget(etp)

        except:
            etp.setText("Bir Hata Olustu!")
            v_box.addWidget(etp)

    def kapat():
        QtWidgets.qApp.quit()

    buton.clicked.connect(lambda : hesap(gram.isChecked(),usd.isChecked,euro.isChecked(),ster.isChecked()))
    buton2.clicked.connect(kapat)
    pencere.setLayout(v_box)
    pencere.setLayout(h_box)
    pencere.setGeometry(430,150,320,250)
    pencere.show()
    sys.exit(app.exec_())

Pencere()
