#Tulostetaan annetun lauseen yksi sana
def hae_sana(mjono,monesko):

    sanat = []
    i = 1                   #loopin apumuuttuja
    sana1 = 0
    while True:
        sana1 = mjono.find(" ",sana1+1)
        if sana1 == -1:
            break
        sanat.append(sana1)
        i += 1
    sanat.append(len(mjono))

    a = 0                   #indeksin arvo
    b = 0                   #indeksin arvo
    c = 0                   #apumuuttuja, määrittää listan indeksin
    d = 0                   #apumuuttuja, jotta tulostus tulee oikein.
    sanoja = []             #sanalista johon tallennetaan sanat, ilman välilyöntejä
    while c < len(sanat):
        b = sanat[c]
        sanoja.append(mjono[a+d:b])
        d = 1
        a = b
        c += 1
    sana = sanoja[monesko]
    return sana