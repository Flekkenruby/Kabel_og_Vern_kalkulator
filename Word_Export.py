import os, math,time, keyboard
from tables import *


def les():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if os.path.exists(current_dir+"\\mal.txt"):
        path=current_dir+r"\mal.txt"
        return path
    else:
        print("Lager filen")
        with open(current_dir+"\\mal.txt", "w+", encoding="utf-8") as file:
            file.write("#Mal for kabel og vern \n"
                        "#Skriv inn hva du vill at skal skrives ut. \n"
                        "#For at du skal skrive inn variabler og formler bruker du disse variablenene: \n"
                        "#{Pavgitt} = avgitt effekt av motoren \n"
                        "#{U} = spenning \n"
                        "#{cos_phi} = cos φ \n"
                        "#{n} = virkningsgrad \n"
                        "#{SI} = startstrømsfaktor \n"
                        "#{forlegning} = forlegningsmetode \n"
                        "#{sikring} = sikring \n"
                        "#{temp} = temperatur \n"
                        "#{isolasjon} = isolasjon \n"
                        "#{kabler} = antall kabler \n"
                        "#{lengde_kabel} = lengde på kabel \n"
                        "#{distanse_kabel} = avstand mellom kabler \n"
                        "#{distanse_tak} = avstand til tak \n"
                        "#{kabelbro} = kabel ligger på kabelbro \n"
                        "#{kabelbro1} = antall kabelbro i høyden \n"
                        "#{kabelbro2} = type kabelbro \n"
                        "#{kabelbro3} = plassering kabelbro \n"
                        "#{krav_spenningsfall} = maks spenningsfall \n"

                        "#{kvadrat} = ledertverrsnitt \n"
                        "#{Iz} = strømføringsevne \n"
                        "#{DeltaU} = spenningsfall i volt \n"
                        "#{deltaU} = spenningsfall i prosent \n"
                        "#{Ib} = belastningsstrøm \n"
                        "#{gruppe_faktor} = gruppefaktor \n"
                        "#{temp_faktor} = temperaturfaktor \n"
                        "#{Iz_tabell} = tabell for Iz \n"
                        "#{temp_tabell} = tabell for tempfaktor \n"
                        "#{gruppe_tabell} = tabell for gruppefaktor \n"

                        "#{karakteristikk_trip} = tripsstrøm \n"
                        "#{karakteristikk_område} = karakteristikkområde \n"
                        "#{karakteristikk} = karakteristikk \n"

                        "#[e]{motorstrøm} = motorstrøm \n"
                        "#[e]{spenningsfall} = spenningsfall \n"
                        "#[e]{spenningsfall_prosent} = spenningsfall i prosent \n"
                        "#[e]{krav_strøm} = krav til strøm \n"
                       
                       
                        "Avgitt effekt av motoren er {Pavgitt}W \n"
                        "Spenningen på motoren er {U}V \n"
                        "Cos er {cos_phi} \n"
                        "Virkningsgrad er {n} \n"
                        "Startstrømsfaktor er {SI} \n"
                        "Forlegningsmetode er {forlegning} \n"
                        "Sikring er {sikring}A \n"
                        "Temperatur er {temp}°C \n"
                        "Isolasjonen er {isolasjon} \n"
                        "Antall kabler er {kabler} \n"
                        "Lengden på kabelen er {lengde_kabel}m \n"
                        "Det er en kabeltykkelse mellom kabelene {distanse_kabel} \n"
                        "Kabelen ligger rett under et tak {distanse_tak} \n"
                        "Kabelen ligger på en kabelbro {kabelbro} \n"
                        "Det er {kabelbro1} Kabelbro i høyden \n"
                        "Kabelbroen er {kabelbro2} \n"
                        "Kabelbroen er {kabelbro3} \n"
                        "Maksimum spenningsfall er {krav_spenningsfall}% \n"

                        "Kvadrat er {kvadrat} \n"
                        "Strømføringsevne er {Iz}A \n"
                        "Spenningsfall i volt er {DeltaU}V \n"
                        "Spenningsfall i prosent er {deltaU}% \n"
                        "Belastningsstrøm er {Ib}A \n"
                        "Gruppefaktor er {gruppe_faktor} \n"
                        "Tempfaktor er {temp_faktor} \n"
                        "Tabbelen for Iz er {Iz_tabell} \n"
                        "Tabellen for Temp_faktor er {temp_tabell} \n"
                        "Tabellen for Gruppe_faktor er {gruppe_tabell} \n"
                        "karakteristikk tripsrøm er {karakteristikk_trip}A \n"
                        "karakteristikk område er {karakteristikk_område} \n"
                        "karakteristikk er {karakteristikk} \n"

                        "[e]{motorstrøm}\n"
                        "[e]{spenningsfall}\n"
                        "[e]{spenningsfall_prosent}\n"
                        "[e]{krav_strøm}\n"
                        )
            path=current_dir+r"\mal.txt"
            return path

def equation(line):
    line = line.split(",")
    line.pop(0)
    time.sleep(1)
    keyboard.press("alt")
    time.sleep(0.5)
    keyboard.press_and_release("n")
    time.sleep(0.5)
    keyboard.press_and_release("e")
    time.sleep(0.5)
    keyboard.press_and_release("i")
    keyboard.release("alt")
    if "1" in line[0]:
        keyboard.write(f"I_B=P_avgitt/(\\sqrt(3)×U×cos(φ)×\\eta)={line[1]}/(\\sqrt(3)×{line[2]}×{line[3]}×{line[4]})={line[5]}A")
    if "2" in line[0]:
        keyboard.write(f"\\Delta U=(\\sqrt(3)×\\rho×M×Ib×cos(φ))/mm^2=(\\sqrt(3)×{0.0175}×{line[1]}×{line[2]}×{line[3]})/{line[4]}={line[5]}V")
    if "3" in line[0]:
        keyboard.write(f"\\Delta u=(\\Delta U)/U*100={line[1]}/{line[2]}*100={line[3]}%")
    if "4" in line[0]:
        keyboard.write(f"I_b≤I_n≤I_z={line[1]}A≤{line[2]}A≤{line[3]}A")
    keyboard.send("enter")

    

def tekstprossesering(Pa, U, Ib, sikring, karakeristikk, Cable_size, Cable_Current, DeltaU, deltaU, isolasjon, kabler, lengde_kabel, distanse_kabel, distanse_tak, kabelbro, kabelbro1, kabelbro2, kabelbro3, krav, gruppe_faktor, temp_faktor,cos_phi, n,temp,SI,forlegning,karakteristikk_område ):
    path = les()
    with open(path, "r", encoding="utf-8") as file:
        filetxt = file.read()
        lines = filetxt.split("\n")
        for i in range(len(lines)):
            if "#" not in lines[i]:
                lines[i] = lines[i].replace("{Pavgitt}",str(Pa))
                lines[i] = lines[i].replace("{U}",str(U))
                lines[i] = lines[i].replace("{cos_phi}",str(cos_phi))
                lines[i] = lines[i].replace("{n}",str(n))
                lines[i] = lines[i].replace("{SI}",str(SI))
                lines[i] = lines[i].replace("{forlegning}",str(forlegning))
                lines[i] = lines[i].replace("{sikring}",str(sikring))
                lines[i] = lines[i].replace("{temp}",str(temp))
                lines[i] = lines[i].replace("{kabler}",str(kabler))
                lines[i] = lines[i].replace("{lengde_kabel}",str(lengde_kabel))
                if distanse_kabel == "J":
                    lines[i] = lines[i].replace("{distanse_kabel}",str(distanse_kabel))
                if distanse_tak == "J":
                    lines[i] = lines[i].replace("{distanse_tak}",str(distanse_tak))
                if kabelbro == "J":
                    lines[i] = lines[i].replace("{kabelbro}",str(kabelbro))
                    lines[i] = lines[i].replace("{kabelbro1}",str(kabelbro1))
                    lines[i] = lines[i].replace("{kabelbro2}",str(kabelbro2))
                    lines[i] = lines[i].replace("{kabelbro3}",str(kabelbro3))
                lines[i] = lines[i].replace("{krav_spenningsfall}",str(krav))
                lines[i] = lines[i].replace("{isolasjon}",str(isolasjon))
                lines[i] = lines[i].replace("{kvadrat}",str(Cable_size))
                lines[i] = lines[i].replace("{Iz}",str(math.ceil(Cable_Current*100)/100))
                lines[i] = lines[i].replace("{DeltaU}",str(math.ceil(DeltaU*100)/100))
                lines[i] = lines[i].replace("{deltaU}",str(math.ceil(deltaU*100)/100))
                lines[i] = lines[i].replace("{Ib}",str(math.ceil(Ib*100)/100))
                lines[i] = lines[i].replace("{gruppe_faktor}",str(gruppe_faktor))
                lines[i] = lines[i].replace("{temp_faktor}",str(temp_faktor))
                lines[i] = lines[i].replace("{karakteristikk}",str(karakeristikk))
                lines[i] = lines[i].replace("{karakteristikk_område}",str(karakteristikk_område))
                if isolasjon == "PVC":
                    lines[i] = lines[i].replace("{Iz_tabell}",str(table_52B_1(forlegning)[1]))
                if isolasjon == "PEX":
                    lines[i] = lines[i].replace("{Iz_tabell}",str(table_52B_1(forlegning)[2]))
                lines[i] = lines[i].replace("{temp_tabell}",str(table_52B_1(forlegning)[3]))
                lines[i] = lines[i].replace("{gruppe_tabell}",str(table_52B_1(forlegning)[4]))

                lines[i] = lines[i].replace("{motorstrøm}",str(f",[1],{Pa},{U},{cos_phi},{n},{math.ceil(Ib*100)/100}"))
                lines[i] = lines[i].replace("{spenningsfall}",str(f",[2],{lengde_kabel}M,{math.ceil(Ib*100)/100}A,{cos_phi},{Cable_size}mm^2,{math.ceil(DeltaU*100)/100}"))
                lines[i] = lines[i].replace("{spenningsfall_prosent}",str(f",[3],{math.ceil(DeltaU*100)/100}V,{U}V,{math.ceil(deltaU*100)/100}"))
                lines[i] = lines[i].replace("{krav_strøm}",str(f",[4],{math.ceil(Ib*100)/100},{sikring},{math.ceil(Cable_Current*100)/100}"))
                lines[i] = lines[i].replace("{I_start}", str(math.ceil(Ib * SI * 100) / 100))
                karakt_lower = {"A": 2, "B": 3, "C": 5, "K": 8, "D": 10}
                lines[i] = lines[i].replace("{karakteristikk_trip}", str(karakt_lower.get(karakeristikk, 0) * sikring))
    lines =[line for line in lines if "#" not in line]

    return lines

def skriv(Pa, U, Ib, sikring, karakeristikk, Cable_size, Cable_Current, DeltaU, deltaU, isolasjon, kabler, lengde_kabel, distanse_kabel, distanse_tak, kabelbro, kabelbro1, kabelbro2, kabelbro3, krav, gruppe_faktor, temp_faktor,cos_phi, n,temp,SI,forlegning,karakteristikk_område):
    lines = tekstprossesering(Pa, U, Ib, sikring, karakeristikk, Cable_size, Cable_Current, DeltaU, deltaU, isolasjon, kabler, lengde_kabel, distanse_kabel, distanse_tak, kabelbro, kabelbro1, kabelbro2, kabelbro3, krav, gruppe_faktor, temp_faktor,cos_phi, n,temp,SI,forlegning,karakteristikk_område )
    print("Skriver om 5 sekunder...")
    time.sleep(5)
    lines =[line for line in lines if "{" not in line]
    for line in lines:
        if "[e]" in line:
            equation(line)
        elif line.split() == "":
            pass
        else:
            for i in range(len(line)):
                keyboard.write(line[i])
            keyboard.send("enter")
