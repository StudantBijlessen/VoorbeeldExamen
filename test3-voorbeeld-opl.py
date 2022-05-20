# test3-voorbeeld
# Gegeven een bestand test3-voorbeeld.txt met naam, code, kring
# De eerste regel bevat de veldnamen.
# Sommige gegevensrecords komen meermaals voor.
# Onderzoek voor de volgende vragen alleen de unieke records.
# Schrijf de namen van een opgevraagde kring met de bijhorende code,
# naar een bestand resultaat-voorbeeld.txt
# Bepaal en toon per kring het aantal leden.

def main():
    gegevens = inlezen('test3-voorbeeld.txt')
    resultaat = maaklijst(gegevens)
    # print(resultaat)
    namen_en_code, gewenste_kring = bepaalnamen(resultaat)
    schrijven(gewenste_kring, namen_en_code, 'resultaat-voorbeeld.txt')


def inlezen(bestand):
    openbestandl = open(bestand, 'r')
    inhoud = openbestandl.readlines()
    openbestandl.close()
    return inhoud


def maaklijst(bronlijst):
    del bronlijst[0]
    # elke record met naam, code en kring in bronlijst
    for i in range(len(bronlijst)):
        bronlijst[i] = bronlijst[i].rstrip()  # alle whitespaces
    # 3 items per record
    setlijst = set(bronlijst)  # unieke records
    nieuwelijst = []
    for elke_record in setlijst:
        nieuwelijst.append(elke_record.split(';'))
    return nieuwelijst


def bepaalnamen(lijst):
    # Welke gegevens hebben we nodig?
    naam_code = []
    kring = {}
    gezochte_kring = input('Van welke kring wil je de namen met code? ')
    for i in range(len(lijst)):
        if lijst[i][2] == gezochte_kring:
            naam_code.append(lijst[i][0] + ' ' + lijst[i][1])
        if lijst[i][2] in kring:
            kring[lijst[i][2]] += 1
        else:
            kring[lijst[i][2]] = 1
    # alle kringen tonen met hun aantal
    for een_kring in kring:
        print(een_kring, kring[een_kring])
    return naam_code, gezochte_kring


def schrijven(gezochte_kring, namenlijst, bestand):
    namenlijst.sort()
    openbestands = open(bestand, 'w')
    openbestands.write('Kring: ' + gezochte_kring + '\n')
    for ind in range(len(namenlijst)):
        openbestands.write(namenlijst[ind] + '\n')
    openbestands.close()


main()
