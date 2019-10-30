import numpy as np
from const import acceleration_of_gravity as g
from const import heat_capacity_water as c
from const import mass_of_ocean as mo

def schaltjahr(y):
    """JO DIGGA!!!"""
    if y % 400 == 0:
        print("Schaltjahr")
    elif y % 100 == 0:
        print("Kein Schaltjahr")
    elif y % 4 == 0:
        print("Schaltjahr")
    else:
        print("Kein Schaltjahr")

def massive(m):
    """Querprodukt eines numpy massives"""
    result = 1
    for x in m: 
        result = result * x
    print(result)

def energie(m,h,v):
    """Gesamte mechanische energie"""
    energy = ((m * v**2)/2) + (m * g * h)
    print(energy)
    
def wochentag(tag,monat,jahr):
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
    
    anzahl_tage = ( jahr - 1900 ) * 365 + ( jahr - 1900 ) // 4
    
    if monat <= 2 and (jahr-1900) % 4 == 0:
        anzahl_tage -= 1
    #print("Protokoll: Schaltjahr, Anzahl Tage minus 1.")

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

#def linse(art,entf):
#    if art == собирающая:
#        if entf > 2F:
#            print(изображение действительное, перевернутое, уменьшенное)
#        if entf < 2F && entf > F
        
def armageddon(m,v):
    """"""
    t = (m * v**2)/(2 * c * mo)
    
    if t >= 50:
        print("kapput")
    if t < 50:
        print("noch", (((c*mo*50)/(0.5*m))**0.5)-v)
        
        
armageddon(1000000,100000000000)