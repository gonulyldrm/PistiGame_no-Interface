from typing import List, Any, Union

print("...OYUN BASLIYOOOOR...")
istembil_kartlari=["karo as","karo 2","karo 3","karo 4","karo 5","karo 6","karo 7","karo8","karo 9","karo 10","karo J","karo O","karo K","kupa as","kupa 2","kupa 3","kupa 4","kupa 5","kupa 6","kupa 7","kupa 8","kupa 9","kupa 10","kupa J","kupa O","kupa K","maca as","maca 2","maca 3","maca 4","maca 5","maca 6","maca 7","maca 8","maca 9","maca 10","maca J","maca O","maca K","sinek as","sinek 2","sinek 3","sinek 4","sinek 5","sinek 6","sinek 7","sinek 8","sinek 9","sinek 10","sinek J","sinek O", "sinek K"]

oyuncukartları=[]
pckartları=[]
oyuncupuanı=0
oyuncukazandıgıkartlar=[]
pcnınkazandıgıkartlar=[]
pcpuanı=0
yer={}
yerdekisonkagit=[]


import random
yer=random.sample(istembil_kartlari,4)
yerdekisonkagit=random.choice(yer)
print("yerdeki son kart:",yerdekisonkagit)
for i in range(6):
    oyuncukartları = random.sample(istembil_kartlari, 4)
    print("oyuncu kartlai:",oyuncukartları)
    pckartları=random.sample(istembil_kartlari,4)

    for y in range(4):
        oyuncununatacagıkart = input("oyuncunun atmak istediği kart:")
        pcnınatacagıkart = random.choice(pckartları)

        if yerdekisonkagit!=oyuncununatacagıkart:
            yerdekisonkagit = oyuncununatacagıkart
            oyuncukartları.remove(yerdekisonkagit)
            print("oyuncunun kartları:",oyuncukartları)
            yer.append(oyuncununatacagıkart)

            if yer==pcnınatacagıkart and oyuncununatacagıkart==pcnınatacagıkart:
                oyuncukazandıgıkartlar.append(oyuncununatacagıkart)
                oyuncukazandıgıkartlar.append(pcnınatacagıkart)
                yer=""
                yerdekisonkagit=""
                print("OYUNCU PİŞTİ YAPTI")
                print("yerdeki son karrt",yerdekisonkagit)
                oyuncupuanı+=10

            elif oyuncununatacagıkart=="sinek J" or oyuncununatacagıkart=="maca J" or oyuncununatacagıkart=="karo J" or oyuncununatacagıkart=="kupa J":
                yer.append(oyuncununatacagıkart)
                oyuncukazandıgıkartlar.extend(yer)
                yer=""
                yerdekisonkagit=""
                print("yerdeki son kart:",yerdekisonkagit)

        elif yerdekisonkagit==oyuncununatacagıkart:
            oyuncukartları.remove(oyuncununatacagıkart)
            print("oyuncunun kartları:",oyuncukartları)
            yer.append(oyuncununatacagıkart)
            oyuncukazandıgıkartlar=yer
            yer=""
            yerdekisonkagit=""

        if yerdekisonkagit!=pcnınatacagıkart:
            pckartları.remove(pcnınatacagıkart)
            yer.append(pcnınatacagıkart)
            yerdekisonkagit=pcnınatacagıkart
            print("yerdeki son kart:",pcnınatacagıkart)

            if yer==oyuncununatacagıkart and pcnınatacagıkart==oyuncununatacagıkart:
                pcnınkazandıgıkartlar.append(oyuncununatacagıkart)
                pcnınkazandıgıkartlar.append(oyuncununatacagıkart)
                yer=""
                yerdekisonkagit=""
                print("PC PİŞTİ YAPTI")
                print("yerdeki son kart",yerdekisonkagit)
                pcpuanı+=10

            elif pcnınatacagıkart=="sinek J" or pcnınatacagıkart=="maca J" or pcnınatacagıkart=="kupa J" or pcnınatacagıkart=="karo J":
                yer.append(pcnınatacagıkart)
                pcnınkazandıgıkartlar.extend(yer)
                yer=""
                yerdekisonkagit=""
                print("yerdeki son kart",yerdekisonkagit)

        elif yerdekisonkagit==pcnınatacagıkart:
            pckartları.remove(oyuncununatacagıkart)
            yer.append(pcnınatacagıkart)
            pcnınkazandıgıkartlar=yer
            yer=""
            yerdekisonkagit=""
            print("yerdeki son kart",yerdekisonkagit)


#puanlama sistemi:
for a in oyuncukazandıgıkartlar:
    #if yer == oyuncununatacagıkart and pcnınatacagıkart == oyuncununatacagıkart:
        #oyuncupuanı+=10
    if oyuncukazandıgıkartlar[a]=="karo as":
        oyuncupuanı+=1
    if oyuncukazandıgıkartlar[a]=="sinek as":
        oyuncupuanı+=1
    if oyuncukazandıgıkartlar[a]=="maca as":
        oyuncupuanı+=1
    if oyuncukazandıgıkartlar[a]=="kupa as":
        oyuncupuanı+=1
    if oyuncukazandıgıkartlar[a]=="sinek 2":
        oyuncupuanı+=2
    if oyuncukazandıgıkartlar[a]=="karo 10":
        oyuncupuanı+=3
    if oyuncukazandıgıkartlar[a]=="karo J":
        oyuncupuanı+=1
    if oyuncukazandıgıkartlar[a]=="sinek J":
        oyuncupuanı+=1
    if oyuncukazandıgıkartlar[a]=="maca J":
        oyuncupuanı+=1
    if oyuncukazandıgıkartlar[a]=="kupa J":
        oyuncupuanı+=1


for b in pcnınkazandıgıkartlar:
    #if yer == oyuncununatacagıkart and pcnınatacagıkart == oyuncununatacagıkart:
        #pcpuanı+=10
    if pcnınkazandıgıkartlar[b]=="karo as":
        pcpuanı+=1
    if pcnınkazandıgıkartlar[b]=="sinek as":
        pcpuanı+=1
    if pcnınkazandıgıkartlar[b]=="kupa as":
        pcpuanı+=1
    if pcnınkazandıgıkartlar[b]=="maca as":
        pcpuanı+=1
    if pcnınkazandıgıkartlar[b]=="sinek 2":
        pcpuanı+=2
    if pcnınkazandıgıkartlar[b]=="karo 10":
        pcpuanı+=3
    if pcnınkazandıgıkartlar[b]=="karo J":
        pcpuanı+=1
    if pcnınkazandıgıkartlar[b]=="sinek J":
        pcpuanı+=1
    if pcnınkazandıgıkartlar[b]=="kupa J":
        pcpuanı+=1
    if pcnınkazandıgıkartlar[b]=="maca J":
        pcpuanı+=1



if len(oyuncukazandıgıkartlar)<len(pcnınkazandıgıkartlar):
    pcpuanı+=3
elif len(oyuncukazandıgıkartlar)>len(pcnınkazandıgıkartlar):
    oyuncupuanı+=3
print("oyuncu puanı:",oyuncupuanı)
print("pc puanı:",pcpuanı)


#oyuna pek aşina değildim oldugu kadar... :)