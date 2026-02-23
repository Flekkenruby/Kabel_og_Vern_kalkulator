import pandas as pd
def table_52B_1(forlegning):
    #info
    #izpvc,izpex,temp,gruppe
    db = pd.DataFrame({
    "A1": ["Isolerte ledere forlagt i instalasjonsrør i en termisk isolert vegg",
         "52B_4","52B_5","52B_14","52B_17"],
    "A2": ["Flerlederkabel forlagt i instalasjonsrør i en termisk isolert vegg",
           "52B_4","52B_5","52B_14","52B_17"],
    "B1": ["Isolerte ledere forlagt i instalasjonsrør på vegg",
           "52B_4","52B_5","52B_14","52B_17"],
    "B2": ["Flerlederkabel forlagt i instalasjonsrør på vegg",
           "52B_4","52B_5","52B_14","52B_17"],
    "C":  ["En eller flerlederkabel montert på vegg",
           "52B_4","52B_5","52B_14","52B_17"],
    "E":  ["Flerlederkabel forlagt i luft",
           "52B_10","52B_12","52B_14","52B_20"]
    })
    col = db[forlegning]
    return col
def table_52B_4(forlegning):
    db = pd.DataFrame({
        "A1": [13.5,18,24,31,42,56,73],
        "A2": [13,17.5,23,29,39,52,68],
        "B1": [15.5,21,28,36,50,68,89],
        "B2": [15,20,27,34,46,62,80],
        "C": [17.5,24,32,41,57,76,96],
        "D1": [18,24,30,38,50,64,82],
        "D2": [19,24,33,41,54,70,92],
    })
    col = db[forlegning]
    return col

def table_52B_5(forlegning):
    db = pd.DataFrame({
        "A1": [17,23,31,40,54,73,95],
        "A2": [16.5,22,30,38,51,68,89],
        "B1": [20,28,37,48,66,88,117],
        "B2": [19.5,26,35,44,60,80,105],
        "C": [22,30,40,52,71,96,119],
        "D1": [21,28,36,44,58,75,96],
        "D2": [23,30,39,49,65,84,107],
    })
    col = db[forlegning]
    return col

def table_52B_10(forlegning):
    db = pd.DataFrame({
        "E": [18.5,25,34,43,60,80,101]
    })
    col = db["E"]
    return col

def table_52B_12(forlegning):
    db = pd.DataFrame({
        "E": [23,32,42,54,75,100,127]
    })
    col = db["E"]
    return col

def table_52B_14(temp,isolasjon):
    db = pd.DataFrame({
        "10": [1.22,1.15],
        "15": [1.17,1.12],
        "20": [1.12,1.08],
        "25": [1.06,1.04],
        "35": [0.94,0.96],
        "40": [0.87,0.91],    
        "45": [0.79,0.87],
        "50": [0.71,0.82],
        "55": [0.61,0.76],
        "60": [0.5,0.71],
        "65": [0,0.65],
        "70": [0,0.58],
        "75": [0,0.5],
        "80": [0,0.41],
    })
    columns = sorted(float(c) for c in db.columns)
    for col in columns:
        if col >= temp:
            temp_col = str(int(col))
            break
    tempr = db[temp_col]
    if isolasjon == "PVC":
        return tempr[0]
    elif isolasjon == "PEX":
        return tempr[1]


def table_52B_15(temp,isolasjon):
    db = pd.DataFrame({
        "10": [1.1,1.07],
        "15": [1.05,1.04],
        "25": [0.95,0.96],
        "30": [0.89,0.93],
        "35": [0.84,0.89],
        "40": [0.77,0.85],    
        "45": [0.71,0.8],
        "50": [0.63,0.76],
        "55": [0.55,0.71],
        "60": [0.45,0.65],
        "65": [0,0.6],
        "70": [0,0.53],
        "75": [0,0.46],
        "80": [0,0.38],
    })
    columns = sorted(float(c) for c in db.columns)
    for col in columns:
        if col >= temp:
            temp_col = str(int(col))
    tempr = db[temp_col]
    if isolasjon == "PVC":
        return tempr[0]
    elif isolasjon == "PEX":
        return tempr[1]

def table_52B_17(forlegning,kabelbro,kabelbro1,kabelbro2,kabelbro3,kabler,distanse,distanse_tak):
    rekkefølge = [1,2,3,4,5,6,7,8,9,12,16,20]    
    db = pd.DataFrame({
        #kabler/ledere forlagt i bunt i luft på en overflate instøpt eller innlkapslet
        1: [1,0.8,0.7,0.65,0.57,0.54,0.52,0.5,0.45,0.41,0.38],
        #kabler/ledere forlagt i et enkelt lag på vegg, gulv, eller på uperforert bro
        2: [1,0.85,0.79,0.75,0.73,0.72,0.72,0.71,0.7, 0, 0],
        #Kabler/ledere forlagt i et enkelt lag festet direkte under en trehimling/tak
        3: [0.95,0.81,0.72,0.68,0.66,0.64,0.63,0.62,0.61, 0, 0],
    })
    #fix imorgen 22.11.2025
    for i in rekkefølge:
        if i >= kabler:
            kabler = i
            break
    kabler = rekkefølge.index(kabler)
    if forlegning == "C" and distanse_tak == "N":
        col = db[2]
        return col[kabler]
    elif forlegning == "C" and distanse_tak == "J":
        col = db[3]
        if col[kabler] == 0:
            raise ValueError("Det er for mange kabler. Vennligst prøv igjen med mindre antall kabler.")
        else:
            return col[kabler]
    else:
        col = db[1]
        return col[kabler]

def table_52B_18(kurser,distance):
    #avstand mellom kurser reduksjons faktor
    #ingen, En kabel diameter, 0.125m, 0.25m, 0.5m
    distance_index = [0.125,0.25,0.5]
    db = pd.DataFrame({
        2: [0.75,0.8,0.85,0.9,0.9],
        3: [0.65, 0.70, 0.75, 0.8, 0.85],
        4: [0.6, 0.6, 0.7, 0.75, 0.8],
        5: [0.55, 0.55, 0.65, 0.7, 0.8],
        6: [0.5, 0.55, 0.6, 0.70, 0.8],
        7: [0.45, 0.51, 0.57, 0.65, 0.75],
        8: [0.43, 0.48, 0.57, 0.65, 0.75],
        9: [0.41, 0.46, 0.55, 0.63, 0.74],
        12: [0.36, 0.42, 0.51, 0.59, 0.71],
        16: [0.29, 0.35, 0.44, 0.53, 0.66],
    })

    #rouding for distance
    for i in range(len(distance_index)):
        if distance <= distance_index[i]:
            distance = distance_index[i]
            break

    #rouding for kurser
    colum_names = sorted(float(c) for c in db.columns)
    for i in colum_names:
        if kurser <= i:
            kurser = i
            break
        
    col = db[int(kurser)]
    return col[distance_index.index(distance)]

def table_52B_20(forlegning,kabelbro,kabelbro1,kabelbro2,kabelbro3,kabler,distanse,distanse_tak):
    #perforerte broer
    #300mm mellom broer i høyden
    #distx1 har en kabel diameter mellom kablene
    rekkefølge = [1,2,3,4,6,9]
    dist10 = pd.DataFrame({
        1: [1, 0.88, 0.82, 0.79, 0.76, 0.73],
        2: [1, 0.87, 0.80, 0.77, 0.73, 0.68],
        3: [1, 0.86, 0.79, 0.76, 0.71, 0.66],
        6: [1, 0.84, 0.77, 0.73, 0.68, 0.64]
    })
    dist11 = pd.DataFrame({
        1: [1, 1, 0.98, 0.95, 0.91],
        2: [1, 0.99, 0.96, 0.92, 0.87],
        3: [1, 0.98, 0.95, 0.91, 0.86]
    })
    #vertikale perforerte broer med 225mm mellom broer mens kablene berører hverandre
    dist20 = pd.DataFrame({
        1: [1, 0.88, 0.82, 0.78, 0.73, 0.72],
        2: [1, 0.88, 0.81, 0.76, 0.71, 0.70],
    })
    dist21 = pd.DataFrame({
        1: [1, 0.91, 0.89, 0.88, 0.87],
        2: [1, 0.91, 0.88, 0.87, 0.85]
    })
    #uperforert horisontal bru med 300mm mellom broer ok kabler som berører hverandre
    dist30 = pd.DataFrame({
        1: [0.97, 0.84, 0.78, 0.75, 0.71, 0.68],
        2: [0.97, 0.83, 0.76, 0.72, 0.68, 0.63],
        3: [0.97, 0.82, 0.75, 0.71, 0.66, 0.61],
        6: [0.97, 0.81, 0.73, 0.69, 0.63, 0.58]
    })
    #stige bru med 300mm mellom broer ok kabler som berører hverandre
    dist40 = pd.DataFrame({
        1: [1, 0.87, 0.82, 0.8, 0.79, 0.78],
        2: [1, 0.86, 0.8, 0.78, 0.76, 0.73],
        3: [1, 0.85, 0.79, 0.76, 0.73, 0.7],
        6: [1, 0.84, 0.77, 0.73, 0.68, 0.64]
    })
    dist41 = pd.DataFrame({
        1: [1, 1, 1, 1, 1,],
        2: [1, 0.99, 0.98, 0.97, 0.96],
        3: [1, 0.98, 0.97, 0.96, 0.93],
    })

    if kabelbro == "J":
        if kabelbro2 == "Perforert":
            if kabelbro3 == "Vertikal":
                if distanse == "N":
                    db = dist20
                elif distanse == "J":
                    db = dist21
            elif kabelbro3 == "Horisontal":
                if distanse == "N":
                    db = dist10
                elif distanse == "J":
                    db = dist11
        elif kabelbro2 == "Uperforert":
            db = dist30
        elif kabelbro2 == "Stige":
            if distanse == "N":
                db = dist40
            elif distanse == "J":
                db = dist41
    
    for i in rekkefølge:
        if i >= kabler:
            kabler = i
            break
    col = db[kabelbro1]
    return col[kabler-1]