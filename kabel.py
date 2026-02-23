import math
from tables import *
import Word_Export
sikringer = [10,13,15,16,20,25,32,40,50,63]
karakt = ["2-3","3-5","5-10","8-12","10-20"]
karaktt = ["A","B","C","K","D"]
kvadrat = [1.5,2.5,4,6,10,16,25]

def karakteristikk(Ib,SI,sikring):
    I_start = Ib*SI

    #list verification
    if not karakt or not karaktt or len(karakt) != len(karaktt):
        raise ValueError("Lists 'karakt' and 'karaktt' must exist and have the same length.")

    #lower trip multiplier
    lower_limits = []
    for k in karakt:
        parts = k.split("-")
        if len(parts) < 2:
            raise ValueError(f"Invalid Karakteristikk value: {k}")
        lower_limits.append(int(parts[0]))

    #Calculate trip points
    trip_points = []
    for limit in lower_limits:
        trip_points.append(limit * sikring)
   
    #build list of diffrences and set invalid to inf
    diffs = []
    for t in trip_points:
        if I_start <= t:
            diff = abs(I_start - t)
        else:
            diff = float('inf')
        diffs.append(diff)
    
    #find Characteristic
    min_index = diffs.index(min(diffs))
    if int((karakt[min_index]).split("-")[0])*sikring > I_start:
        return karaktt[min_index]
    else:
        raise ValueError(f"For høy startstrøm {I_start}")

def karakteristikk_område(karakteristikk):
    index = karaktt.index(karakteristikk)
    return karakt[index]

def kabel(forlegning, sikring, temp, isolasjon, kabler, kabelbro, kabelbro1, kabelbro2, kabelbro3, distanse_kabel, distanse_tak, lengde_kabel, Ib, krav, U):
    col = None
    #forlegning
    main = table_52B_1(forlegning)
    if isolasjon == "PVC":
        call = "table_"+str(main[1])
        func = globals().get(call)
        if func is None:
            raise ValueError(f"Invalid function name: {call}")
        col = func(forlegning)
    elif isolasjon == "PEX":
        call = "table_"+str(main[2])
        func = globals().get(call)
        if func is None:
            raise ValueError(f"Invalid function name: {call}")
        col = func(forlegning)

    #temp faktor
    if temp == "N/A":
        temp_faktor = 1
    else:
        if isolasjon == "PVC":
            if temp <= 60:
                call = "table_"+str(main[3])
                func = globals().get(call)
                if func is None:
                    raise ValueError(f"Invalid function name: {call}")
                temp_faktor = func(temp,isolasjon)
            else:
                print("PVC kan ikke ha temperatur over 60°C")
                print("Bytter insolasjon til PEX")
                isolasjon = "PEX"
                call = "table_"+str(main[3])
                func = globals().get(call)
                if func is None:
                    raise ValueError(f"Invalid function name: {call}")
                temp_faktor = func(temp,isolasjon)
        elif isolasjon == "PEX":
            call = "table_"+str(main[3])
            func = globals().get(call)
            if func is None:
                raise ValueError(f"Invalid function name: {call}")
            temp_faktor = func(temp,isolasjon)
            if temp_faktor == 0 or temp_faktor == None:
                temp_faktor = 1
                print("Temperatur er ikke tatt med i kalkulasjonen")

    #gruppe faktor
    call = "table_"+str(main[4])
    func = globals().get(call)
    if func is None:
        raise ValueError(f"Invalid function name: {call}")
    gruppe_faktor = func(forlegning,kabelbro,kabelbro1,kabelbro2,kabelbro3,kabler,distanse_kabel,distanse_tak)
    if gruppe_faktor == 0 or gruppe_faktor == None:
        raise ValueError("Det er for mange kabler. Vennligst prøv igjen med mindre antall kabler.")
    for i in range(len(col)):
        Iz = col[i]*temp_faktor*gruppe_faktor
        if Iz>= sikring:
            if lengde_kabel > 0:
                DeltaU = (math.sqrt(3)*0.0175*lengde_kabel*Ib)/kvadrat[i]
                deltaU = (DeltaU)/U*100
                if deltaU < krav:
                    return [kvadrat[i],Iz,DeltaU,deltaU,temp_faktor,gruppe_faktor]
            else:
                return [kvadrat[i],Iz,0,0,temp_faktor,gruppe_faktor]
            
while True:
    try:
        sikring = None
        kabelbro1 = None
        kabelbro2 = None
        kabelbro3 = None
        distanse_kabel = None
        krav = None
        print("Dette er et prosjekt som er under arbeid. Ta infoene med en klype salt.")
        print("Vennligst skriv inn de nødvendige informasjonene: ")
        Pa = input("Skriv inn Pavgitt (W): ")
        U = input("Skriv inn spenning U (V): ")
        cos_phi = input("Skriv inn cos φ: ")
        n = input("Skriv inn virkningsgrad n: ")
        SI = input("Skriv inn startstrømsfaktor SI (standard 1): ")
        forlegning = input("Skriv inn forlegningsmetode (f.eks. A1, C): ").upper()
        temp = input("Skriv inn omgivelsestemperatur (°C, standard N/A): ")
        isolasjon = input("Skriv inn isolasjonstype (PVC, PEX, standard PVC): ").upper()
        kabler = input("Hvor mange kabler er i gruppen? (standard 1): ")
        lengde_kabel = input("Hvor lang er kabelen? (m, standard 0): ")
        lengde_kabel = float(lengde_kabel) if lengde_kabel else 0
        if int(lengde_kabel) > 0:
            krav = input("hva er maks spenningsfall i prosent? (standard 5%): ")
        kabelbro = input("Ligger kabelen på en kabelbro? (J/N): Standard N: ").upper()
        distanse_tak = input("Ligger kabelen direkte under et tak? (J/N): Standard N: ").upper()

        kabelbro = "N" if kabelbro == "" else kabelbro
        if kabelbro == "J" or kabelbro == "Y":
            kabelbro1 = input("Hvor mange broer er stablet oppå hverandre? (standard 1): ")
            kabelbro2 = input("Hvilken type bro er det (standard Uperforert): ").capitalize()
            kabelbro3 = input("Er broen horisontal eller vertikal? (standard horisontal): ").capitalize()
            if forlegning == "E":
                distanse_kabel = input("Er det en kabeltykkelse mellom kablene? (J/N): Standard N: ").upper()
        kabelbro1 = int(kabelbro1) if kabelbro1 else 1
        kabelbro2 = kabelbro2 if kabelbro2 else "Uperforert"
        kabelbro3 = kabelbro3 if kabelbro3 else "Horisontal"
        distanse_kabel = distanse_kabel if distanse_kabel else "N"
        krav = int(krav) if krav else 5

            

        # Apply defaults
        SI = int(SI) if SI else 1
        temp = int(temp) if temp and temp != "N/A" else "N/A" 
        isolasjon = isolasjon if isolasjon else "PVC"
        kabler = int(kabler) if kabler else 1
        distanse_tak = distanse_tak if distanse_tak else "N"
        
        

        # Convert numeric inputs
        Pa = int(Pa)
        U = int(U)
        cos_phi = float(cos_phi)
        n = float(n)

        Ib = Pa / (math.sqrt(3) * U * cos_phi * n)

        # Select fuse
        while sikring is None:
            for i in range(len(sikringer)):
                if sikringer[i] >= Ib:
                    sikring = sikringer[i]
                    break

        # Print results
        cable_size, cable_current, DeltaU, deltaU, temp_faktor, gruppe_faktor = kabel(forlegning, sikring, temp, isolasjon, kabler, kabelbro, kabelbro1, kabelbro2, kabelbro3, distanse_kabel, distanse_tak, lengde_kabel, Ib, krav, U)
        if cable_current == 0:
            raise ValueError("Det er for mange kabler. Vennligst prøv igjen med mindre antall kabler.")
        print(
            f"Ib = {math.ceil(Ib*100)/100}A, \n"
            f"Sikring = {sikring}A, \n"
            f"Karakteristikk = {karakteristikk(Ib, SI, sikring)}, \n"
            f"Kabel = {math.ceil(cable_size*100)/100}mm², \n"
            f"Iz = {math.ceil(cable_current*100)/100}A, \n"
            f"ΔU = {math.ceil(DeltaU*100)/100}V, \n"
            f"Δu = {math.ceil(deltaU*100)/100}%"
        )
        a = input("Vill du skrive inn i word? (J/N): ").upper()
        if a == "J":
            Word_Export.skriv(Pa, U, Ib, sikring, karakteristikk(Ib, SI, sikring), cable_size, cable_current, DeltaU, deltaU, isolasjon, kabler, lengde_kabel, distanse_kabel, distanse_tak, kabelbro, kabelbro1, kabelbro2, kabelbro3, krav, gruppe_faktor, temp_faktor,cos_phi, n,temp,SI,forlegning,karakteristikk_område(forlegning))
            print("Programmet er ferdig å skrive.")
            #Pa, U, Ib, sikring, karakeristikk, Cable_size, Cable_Current, DeltaU, deltaU, isolasjon, kabler, lengde_kabel, distanse_kabel, distanse_tak, kabelbro, kabelbro1, kabelbro2, kabelbro3, krav, kvadrat, gruppe_faktor, temp_faktor 
    except Exception as e:
        print("Error:", e)
    except ValueError as e:
        print("Value Error:", e)
    finally:
        print("Programmet er avsluttet.")
        
