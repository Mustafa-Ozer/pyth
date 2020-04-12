import sys
from PyQt5 import QtWidgets
from datetime import datetime
from bs4 import BeautifulSoup
import requests

try:
    def veri_cek():
        url = "https://covid19.saglik.gov.tr/"
        response = requests.get(url)
        html_ic = response.content
        soup = BeautifulSoup(html_ic,"html.parser")
        deger = soup.find_all("span")
        value = list()
        baslik = list()
        detay = list()
        t=0
        for i in deger:   
            for x in i:
                if(str(x)!="<br/>"):
                    try:
                        if(float(x)!= 33.17 and t==0):
                            value.append(float(x))
                        else:
                            t=1                            
                    except:
                        if(str(x).replace(" ","").replace("\n","").replace("\r","")=="BUGÜNKÜ"):
                            break
                        baslik.append(str(x).replace(" ","").replace("\n","").replace("\r",""))
        bir=baslik[0].strip()+" "+baslik[1].strip()+" "+baslik[2].strip()+" "+":"+" "+str(int(value[0]*1000))
        iki=baslik[3].strip()+" "+baslik[4].strip()+" "+baslik[5].strip()+" "+":"+" "+str(int(value[1]*1000))
        uc=baslik[6].strip()+" "+baslik[7].strip()+" "+baslik[8].strip()+" "+":"+" "+str(int(value[2]*1000))
        dort=baslik[9].strip()+" "+baslik[10].strip()+" "+baslik[11].strip()+" "+":"+" "+str(int(value[3]*1000))
        bes=baslik[12].strip()+" "+baslik[13].strip()+" "+baslik[14].strip()+" "+":"+" "+str(int(value[4]*1000))
        alti=baslik[15].strip()+" "+baslik[16].strip()+" "+baslik[17].strip()+" "+":"+" "+str(int(value[5]*1000))
        ls=[bir,iki,uc,dort,bes,alti]
        return ls

            
    
                
    a=0        
    for i in veri_cek():
        if(a==0):
            bir=i
        elif(a==1):
            iki=i
        elif(a==2):
            uc=i
        elif(a==3):
            dort=i
        elif(a==4):
            bes=i
        elif(a==5):
            alti=i
        a+=1
                
                
    def veri_cek2():
        url = "https://covid19.saglik.gov.tr/"
        response = requests.get(url)
        html_ic = response.content
        soup = BeautifulSoup(html_ic,"html.parser")
        tarih=soup.find_all("div",{"class":"takvim text-center"})
        dd=list()
        for i in tarih:
            for x in i:
                for j in x:
                    dd.append(j)
        return dd
    tarih=""
    for i in veri_cek2():
        if(str(i)!="\n"):
            tarih+=i+" "

except:
    a="nc"
    print("Hata")


def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Covid-19")
    h_box = QtWidgets.QHBoxLayout()
    v_box = QtWidgets.QVBoxLayout()
    etiket = QtWidgets.QLabel(pencere)
    etiket.setText("\tCOVID-19 VERILERI(TURKIYE)")
    etiket.move(160,50)
    if(a!="nc"):
        etiket2=QtWidgets.QLabel(pencere)
        etiket2.setText(
        """
\t          {}\n  
    -------------------------------------------------
        
            {}
                
            {}
                
            {}
        
{}

    {}

    {}
            
    -------------------------------------------------
    
            Kaynak : covid19.saglik.gov.tr
        """
            .format(tarih,bir,iki,uc,dort,bes,alti))
        etiket2.move(80,120)
    else:
        etiket2 = QtWidgets.QLabel(pencere)
        etiket2.setText("BAGLANTI YOK")
        etiket2.move(200,150)
    v_box.addStretch()
    v_box.addWidget(etiket)
    v_box.addWidget(etiket2)
    v_box.addStretch()
    h_box.addStretch()
    h_box.addLayout(v_box)
    h_box.addStretch()
    pencere.setLayout(h_box)
    pencere.setGeometry(400,150,320,250)
    pencere.show()
    sys.exit(app.exec_())

Pencere()
    
    
