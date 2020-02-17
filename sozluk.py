def tk(x,y):
    x = x[:-1]
    liste = x.split(",")
    turkce = liste[0]
    ingilizce = liste[1]
    if(y==turkce):
        print(ingilizce)
    elif(y==ingilizce):
        print(turkce)
    
print("""
*********************************************
Sözlük Oluşturma Programına Hoşgeldiniz.    *
     İŞLEMLER                               *
1.Kelime ekle                               *
2.Kelime ara                                *
3.Çıkmak için q                             *
                                            *
*********************************************
""")
while True:
    ls=list()
    a=input("İşlem seç(1,2,q) : ")
    if(a=="1"):
        with open("sozluk.txt","a",encoding = "utf-8") as file:
            a = input("Kelimenin Türkçesini Gir : ")
            b = input("Kelimenin İngilizcesini Gir : ")
            file.write(a+","+b+"\n")
    elif(a=="2"):
        with open("sozluk.txt","r",encoding = "utf-8") as file:
            d = input("Aradığın kelimenin Türkçesini yada İngilizcesini gir : ")
            for i in file:
                ls.append(tk(i,d))
    elif(a=="q"):
        break
    
    
