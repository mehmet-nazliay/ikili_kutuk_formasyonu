import sqlite3


baglanti=sqlite3.connect("ciktilar.db")
isaretci=baglanti.cursor()
isaretci.execute("create table if not exists results (tip TEXT,yon TEXT, date  TEXT, high38th NUMERIC, low38thlow NUMERIC, after36high NUMERIC, after36low NUMERIC, target NUMERIC, losess NUMERIC,oncelik TEXT,before36max NUMERIC,before36min NUMERIC)")
baglanti.commit()




con=sqlite3.connect("veriyeni.db")

db=con.cursor()

cek=db.execute("SELECT * from yen")

listetarih=[]
listeopen=[]
listehigh=[]
listelow=[]
listeclose=[]


for i in cek:
    listetarih.append(i[4])
    listeopen.append(i[0])
    listehigh.append(i[2])
    listelow.append(i[3])
    listeclose.append(i[1])
    
    
    
a=len(listetarih)
b=a-36



liste18=[]
liste17=[]           
for i in range(0,b):   
    #tek bar artıştan azalışa dönüş
    if listeopen[i]<listeclose[i]:
        liste18.append(i)
        if (i+36)>b:
            continue
        if (max(liste18)-min(liste18))==36:
            del liste18[0:100]
        elif len(liste18)==18:
            del liste18[0:18]        
            if (listeopen[i+37]>listeclose[i+37]) and (listeopen[i+36]<listeclose[i+36]):
                vr=(max(listehigh[0+i:35+i])-min(listelow[0+i:35+i]))
                vr37=(listehigh[37+i]-listelow[37+i])
                if vr37>=vr*0.2:
                    if (i+36)>b:
                        continue
                    bartarih=listetarih[i+37]
                    bar38high=listehigh[i+37]
                    bar38low=listelow[i+37]
                    bar38close=listeclose[i+37]
                    bar36afterhightek=max(listehigh[i+38:i+74])
                    bar36afterlowtek=min(listelow[i+38:i+74])
                    before36max=max(listehigh[i:i+35])
                    before36min=min(listelow[i:i+35])
                    yon="azalis"
                    target=bar38close-bar36afterlowtek
                    losess=bar36afterhightek-bar38close
                    tip="Tek"
                    print("""********Tek Bar********""",i)
                    listeoncelik1=[]
                    listeoncelik2=[]            
                    for j in range(38,74):
                        listeoncelik1.append(listelow[i+j])
                        listeoncelik2.append(listehigh[i+j])
                    o1=listeoncelik1.index(min(listeoncelik1))
                    o2=listeoncelik2.index(max(listeoncelik2))
                    if o2>o1:
                        oncelik="1.target"
                    elif o2<o1:
                        oncelik="1.losess"
                    insert_stmt=("""INSERT INTO results
(tip, yon, date, high38th, low38thlow, after36high, after36low, target, losess, oncelik, before36max, before36min) 
Select ?,?,?,?,?,?,?,?,?,?,?,?
WHERE NOT EXISTS (SELECT 1 FROM results WHERE tip=? and yon=? and date=? and high38th=? and low38thlow=? and after36high=? and after36low=? and target=? and losess=? and oncelik=? and before36max=? and before36min=?)""")
                    isaretci.execute(insert_stmt,(tip, yon, bartarih, bar38high, bar38low, bar36afterhightek, bar36afterlowtek, target, losess, oncelik, before36max, before36min)*2)
                    baglanti.commit()
        #çift bar artıştan azalışa dönüş
            elif (listeopen[i+38]>listeclose[i+38]) and (listeopen[i+36]<listeclose[i+36]) and (listeopen[i+37]<listeclose[i+37]):
                vr=(max(listehigh[0+i:35+i])-min(listelow[0+i:35+i]))
                vr37=(listehigh[38+i]-listelow[37+i])
                if vr37>=vr*0.2:
                    if (i+36)>b:
                        continue
                    bartarih=listetarih[i+38]
                    bar38high=listehigh[i+38]
                    bar38close=listeclose[i+38]
                    bar38low=listelow[i+38]
                    bar36afterhightek=max(listehigh[i+39:i+75])
                    bar36afterlowtek=min(listelow[i+39:i+75])
                    before36max=max(listehigh[i:i+35])
                    before36min=min(listelow[i:i+35])
                    yon="azalis"
                    target=bar38close-bar36afterlowtek
                    losess=bar36afterhightek-bar38close
                    tip="cift"
                    print("""********Çift Bar********""",i)
                    listeoncelik1=[]
                    listeoncelik2=[]            
                    for j in range(39,75):
                        listeoncelik1.append(listelow[i+j])
                        listeoncelik2.append(listehigh[i+j])
                    o1=listeoncelik1.index(min(listeoncelik1))
                    o2=listeoncelik2.index(max(listeoncelik2))
                    if o2>o1:
                        oncelik="1.target"
                    elif o2<o1:
                        oncelik="1.losess"
                    insert_stmt=("""INSERT INTO results
(tip, yon, date, high38th, low38thlow, after36high, after36low, target, losess, oncelik, before36max, before36min) 
Select ?,?,?,?,?,?,?,?,?,?,?,?
WHERE NOT EXISTS (SELECT 1 FROM results WHERE tip=? and yon=? and date=? and high38th=? and low38thlow=? and after36high=? and after36low=? and target=? and losess=? and oncelik=? and before36max=? and before36min=?)""")
                    isaretci.execute(insert_stmt,(tip, yon, bartarih, bar38high, bar38low, bar36afterhightek, bar36afterlowtek, target, losess, oncelik, before36max, before36min)*2)
                    baglanti.commit()
        #üçlü bar artıştan azalışa dönüş
            elif (listeopen[i+39]>listeclose[i+39]) and (listeopen[i+36]<listeclose[i+36]) and (listeopen[i+37]<listeclose[i+37]) and (listeopen[i+38]<listeclose[i+38]):
                vr=(max(listehigh[0+i:35+i])-min(listelow[0+i:35+i]))
                vr37=(listehigh[39+i]-listelow[37+i])
                if vr37>=vr*0.2:
                    if (i+36)>b:
                        continue
                    bartarih=listetarih[i+39]
                    bar38high=listehigh[i+39]
                    bar38low=listelow[i+39]
                    bar38close=listeclose[i+39]
                    bar36afterhightek=max(listehigh[i+40:i+76])
                    bar36afterlowtek=min(listelow[i+40:i+76])
                    before36max=max(listehigh[i:i+35])
                    before36min=min(listelow[i:i+35])
                    yon="azalis"
                    target=bar38close-bar36afterlowtek
                    losess=bar36afterhightek-bar38close
                    tip="uclu"
                    print("""********Üçlü Bar********""",i)
                    listeoncelik1=[]
                    listeoncelik2=[]            
                    for j in range(40,76):
                        listeoncelik1.append(listelow[i+j])
                        listeoncelik2.append(listehigh[i+j])
                    o1=listeoncelik1.index(min(listeoncelik1))
                    o2=listeoncelik2.index(max(listeoncelik2))
                    if o2>o1:
                        oncelik="1.target"
                    elif o2<o1:
                        oncelik="1.losess"
                    insert_stmt=("""INSERT INTO results
(tip, yon, date, high38th, low38thlow, after36high, after36low, target, losess, oncelik, before36max, before36min) 
Select ?,?,?,?,?,?,?,?,?,?,?,?
WHERE NOT EXISTS (SELECT 1 FROM results WHERE tip=? and yon=? and date=? and high38th=? and low38thlow=? and after36high=? and after36low=? and target=? and losess=? and oncelik=? and before36max=? and before36min=?)""")
                    isaretci.execute(insert_stmt,(tip, yon, bartarih, bar38high, bar38low, bar36afterhightek, bar36afterlowtek, target, losess,oncelik, before36max, before36min)*2)
                    baglanti.commit()
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    

    #tek bar azalıştan artışa dönüş
    elif listeopen[i]>listeclose[i]:
        liste17.append(i)
        if (i+36)>b:
            continue
        
        if (max(liste17)-min(liste17))==36:
            del liste17[0:100]
        elif len(liste17)==18:
            del liste17[0:18]        
            if (listeopen[i+37]<listeclose[i+37]) and (listeopen[i+36]>listeclose[i+36]):
                vr=(max(listehigh[0+i:35+i])-min(listelow[0+i:35+i]))
                vr37=(listehigh[37+i]-listelow[37+i])
                if vr37>=vr*0.2:
                    if (i+36)>b:
                        continue
                    bartarih=listetarih[i+37]
                    bar38high=listehigh[i+37]
                    bar38low=listelow[i+37]
                    bar38close=listeclose[i+37]
                    bar36afterhightek=max(listehigh[i+38:i+74])
                    bar36afterlowtek=min(listelow[i+38:i+74])
                    before36max=max(listehigh[i:i+35])
                    before36min=min(listelow[i:i+35])
                    yon="artis"
                    target=bar36afterhightek-bar38close
                    losess=bar38close-bar36afterlowtek
                    tip="Tek"
                    print("""********Tek Bar********""",i)
                    listeoncelik1=[]
                    listeoncelik2=[]            
                    for j in range(38,74):
                        listeoncelik1.append(listelow[i+j])
                        listeoncelik2.append(listehigh[i+j])
                    o1=listeoncelik1.index(min(listeoncelik1))
                    o2=listeoncelik2.index(max(listeoncelik2))
                    if o2<o1:
                        oncelik="1.target"
                    elif o2>o1:
                        oncelik="1.losess"
                    insert_stmt=("""INSERT INTO results
(tip, yon, date, high38th, low38thlow, after36high, after36low, target, losess, oncelik, before36max, before36min) 
Select ?,?,?,?,?,?,?,?,?,?,?,?
WHERE NOT EXISTS (SELECT 1 FROM results WHERE tip=? and yon=? and date=? and high38th=? and low38thlow=? and after36high=? and after36low=? and target=? and losess=? and oncelik=? and before36max=? and before36min=?)""")
                    isaretci.execute(insert_stmt,(tip, yon, bartarih, bar38high, bar38low, bar36afterhightek, bar36afterlowtek, target, losess, oncelik, before36max, before36min)*2)
                    baglanti.commit()
                    
                    
                    
                    
            elif (listeopen[i+38]<listeclose[i+38]) and (listeopen[i+36]>listeclose[i+36]) and (listeopen[i+37]>listeclose[i+37]):
                vr=(max(listehigh[0+i:35+i])-min(listelow[0+i:35+i]))
                vr37=(listehigh[38+i]-listelow[37+i])
                if vr37>=vr*0.2:
                    if (i+36)>b:
                        continue
                    bartarih=listetarih[i+38]
                    bar38high=listehigh[i+38]
                    bar38low=listelow[i+38]
                    bar38close=listeclose[i+38]
                    bar36afterhightek=max(listehigh[i+39:i+75])
                    bar36afterlowtek=min(listelow[i+39:i+75])
                    before36max=max(listehigh[i:i+35])
                    before36min=min(listelow[i:i+35])
                    yon="artis"
                    target=bar36afterhightek-bar38close
                    losess=bar38close-bar36afterlowtek
                    tip="cift"
                    print("""********Çift Bar********""",i)
                    listeoncelik1=[]
                    listeoncelik2=[]            
                    for j in range(39,75):
                        listeoncelik1.append(listelow[i+j])
                        listeoncelik2.append(listehigh[i+j])
                    o1=listeoncelik1.index(min(listeoncelik1))
                    o2=listeoncelik2.index(max(listeoncelik2))
                    if o2<o1:
                        oncelik="1.target"
                    elif o2>o1:
                        oncelik="1.losess"
                    insert_stmt=("""INSERT INTO results
(tip, yon, date, high38th, low38thlow, after36high, after36low, target, losess, oncelik, before36max, before36min) 
Select ?,?,?,?,?,?,?,?,?,?,?,?
WHERE NOT EXISTS (SELECT 1 FROM results WHERE tip=? and yon=? and date=? and high38th=? and low38thlow=? and after36high=? and after36low=? and target=? and losess=? and oncelik=? and before36max=? and before36min=?)""")
                    isaretci.execute(insert_stmt,(tip, yon, bartarih, bar38high, bar38low, bar36afterhightek, bar36afterlowtek, target, losess, oncelik, before36max, before36min)*2)
                    baglanti.commit()
                    
            elif (listeopen[i+39]<listeclose[i+39]) and (listeopen[i+36]>listeclose[i+36]) and (listeopen[i+37]>listeclose[i+37]) and (listeopen[i+38]>listeclose[i+38]):
                vr=(max(listehigh[0+i:35+i])-min(listelow[0+i:35+i]))
                vr37=(listehigh[39+i]-listelow[37+i])
                if vr37>=vr*0.2:
                    if (i+36)>b:
                        continue
                    bartarih=listetarih[i+39]
                    bar38high=listehigh[i+39]
                    bar38low=listelow[i+39]
                    bar38close=listeclose[i+38]
                    bar36afterhightek=max(listehigh[i+40:i+76])
                    bar36afterlowtek=min(listelow[i+40:i+76])
                    before36max=max(listehigh[i:i+35])
                    before36min=min(listelow[i:i+35])
                    yon="artis"
                    target=bar36afterhightek-bar38close
                    losess=bar38close-bar36afterlowtek
                    tip="uclu"
                    print("""********Üçlü Bar********""",i)
                    listeoncelik1=[]
                    listeoncelik2=[]            
                    for j in range(40,76):
                        listeoncelik1.append(listelow[i+j])
                        listeoncelik2.append(listehigh[i+j])
                    o1=listeoncelik1.index(min(listeoncelik1))
                    o2=listeoncelik2.index(max(listeoncelik2))
                    if o2<o1:
                        oncelik="1.target"
                    elif o2>o1:
                        oncelik="1.losess"
                    insert_stmt=("""INSERT INTO results
(tip, yon, date, high38th, low38thlow, after36high, after36low, target, losess, oncelik, before36max, before36min) 
Select ?,?,?,?,?,?,?,?,?,?,?,?
WHERE NOT EXISTS (SELECT 1 FROM results WHERE tip=? and yon=? and date=? and high38th=? and low38thlow=? and after36high=? and after36low=? and target=? and losess=? and oncelik=? and before36max=? and before36min=?)""")
                    isaretci.execute(insert_stmt,(tip, yon, bartarih, bar38high, bar38low, bar36afterhightek, bar36afterlowtek, target, losess, oncelik, before36max, before36min)*2)
                    baglanti.commit()



baglanti.close()    