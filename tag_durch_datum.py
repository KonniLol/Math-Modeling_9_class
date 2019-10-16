# V A R I A B L E N
januar =31
februar =28
maerz = 31
april =30
mai = 31
juni = 30
juli = 31
august = 31
september = 30
oktober =31
november = 30
dezember = 31



# E I N G A B E
tag = int(input("Bitte geben Sie den Tag (1 bis 31) ein: "))
monat = int(input("Bitte geben Sie den Monat (1 bis 12) ein: "))
jahr = int(input("Bitte geben Sie das Jahr ein: "))

# B E R E C H N U N G
anzahl_tage = ( jahr - 1900 ) * 365 + ( jahr - 1900 ) // 4


if monat <= 2 and (jahr-1900) % 4 == 0:
    anzahl_tage -= 1
    print("Protokoll: Schaltjahr, Anzahl Tage minus 1.")

if monat == 1:
        anzahl_tage += tag 
elif monat == 2:
        anzahl_tage += januar + tag 
elif monat == 3:
        anzahl_tage += januar + februar + tag 
elif monat == 4:
        anzahl_tage += januar + februar + maerz + tag  
elif monat == 5:
        anzahl_tage += januar + februar + maerz + april + tag 
elif monat == 6:
        anzahl_tage += januar + februar + maerz + april + mai + tag 
elif monat == 7:
        anzahl_tage += januar + februar + maerz + april + mai + juni + tag 
elif monat == 8:
        anzahl_tage += januar + februar + maerz + april + mai + juni + juli + tag 
elif monat == 9:
        anzahl_tage += januar + februar + maerz + april + mai + juni + juli + august + tag 
elif monat == 10:
        anzahl_tage += januar + februar + maerz + april + mai + juni + juli + august + september + tag 
elif monat == 11 :   
        anzahl_tage += januar + februar + maerz + april + mai + juni + juli + august + september + oktober + tag 
elif monat == 12:
        anzahl_tage += januar + februar + maerz + april + mai + juni + juli + august + september + oktober + november + tag 
#print(anzahl_tage)
wochentag = anzahl_tage  % 7


# A U S G A B E 
 
if wochentag == 0:
    print("Sonntag")
elif wochentag == 1:
    print("Montag")
elif wochentag == 2:
    print("Dienstag")
elif wochentag == 3:
    print("Mittwoch")
elif wochentag == 4:
    print("Donnerstag")
elif wochentag == 5:
    print("Freitag")
elif wochentag == 6:
    print("Samstag")
else:
    print("Fehler")