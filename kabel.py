import math
import pandas as pd
sikringer = [10,13,15,16,20,25,32,40,50,63]
karakt = ["2-3","3-5","5-10","8-12","10-20"]
karaktt = ["A","B","C","K","D"]
sikring = None
kvadrat = [1.5,2.5,4,6,10]
def table_52B_1():
    pass
def table_52B_2_CU(forlegning):
    db = pd.DataFrame({
        "A1": [14.5,19.5,26,34,46],
        "A2": [14,18.5,25,32,43],
        "B1": [17.5,24,32,41,57],
        "B2": [16.5,23,30,38,52],
        "C": [19.5,27,36,46,63],
        "D1": [22,27,37,46,60],
        "D2": [22,28,38,48,64]
    })
    col = db[forlegning]
    return col

def table_52B_17(temp,isolasjon):
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
    

def karakteristikk(Ib,SI):
    Ibt = Ib * SI
    kt = []
    kd = []
    pop = []
    for i in range(len(karakt)):
        k = karakt[i]
        k = k.split('-')
        k.pop(1)
        k = int(k[0])
        kt.append(k*sikring)
    for i in range(len(kt)):
        kd.append(Ibt-kt[i])
    for i in range(len(kd)):
        if kd[i] > 0:
            pop.append(i)
    kd = [1000 if i in pop else x for i, x in enumerate(kd)]
    kd = [abs(x) for x in kd]
    test = min(kd)
    test2 = kd.index(test)
    return karaktt[test2]

def kabel(forlegning,sikring,temp,isolasjon):
    col = table_52B_2_CU(forlegning)
    temp = table_52B_17(temp,isolasjon)
    gruppe = 1
    for i in range(len(col)):
        x = col[i]*temp*gruppe
        if x >= sikring:
            return [x,kvadrat[i]]
        
while True:
    parameters = input("Pavgitt, U, cos, n, SI, forlegning, temp, isolasjon"+ "\n")
    if parameters is not None:
        parameters = parameters.split(', ')
        Pa = parameters[0]
        U = parameters[1]
        cos = parameters[2]
        n = parameters[3]
        SI = parameters[4]
        forlegning = parameters[5]
        temp = parameters[6]
        isolasjon = parameters[7]
        Pa = int(Pa)
        U = int(U)
        cos = float(cos)
        n = float(n)
        SI = int(SI)
        temp = int(temp)
        Ib = Pa/(math.sqrt(3)*U*cos*n)
        while sikring is None:
            for i in range(len(sikringer)):
                if sikringer[i] >= Ib:
                    sikring = sikringer[i]
                    break
        print(str((math.ceil(Ib*100)/100))+"A "+ str(sikring)+"A "+karakteristikk(Ib,SI)+" "+str((math.ceil(kabel(forlegning,sikring,temp,isolasjon)[1]*100)/100))+"mm²"+" "+str((math.ceil(kabel(forlegning,sikring,temp,isolasjon)[0]*100)/100))+"A")
        parameters = None
