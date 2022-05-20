def main():
    try:
        records = leesInput('test3-voorbeeld2.txt')
        records = leesInput('test3-voorbeeld2.txt')

        kring = input('Van welke kring wil je de leden afdrukken?')
        print(f'Je hebt gekozen voor {kring}!')
        print_kring_leden(records, kring)
        aantal_leden_per_kring(records)

    except Exception as e:
        print(e)
        print('Zorg voor de juiste input!')


def bestaat(records, record):
    record_bestaat = False
    for current_record in records:
        for i in range(len(records)):
            if current_record == record:
                record_bestaat = True

    return record_bestaat


def leesInput(filename):
    with open(filename, 'r') as input_file:
        veldnamen = input_file.readline().rstrip('\n')
        veldnamen = veldnamen.split(';')

        records = list()

        lineNr = 2
        for line in input_file.readlines():
            line = line.rstrip('\n')

            record_elements = line.split(';')

            if len(record_elements) != len(veldnamen):
                raise Exception(
                    f'Lijn {lineNr}: aantal veldnamen moet {len(veldnamen)} zijn, maar is {len(record_elements)}')

            new_record = \
                {
                    veldnamen[0]: record_elements[0],
                    veldnamen[1]: record_elements[1],
                    veldnamen[2]: record_elements[2]
                }

            record_bestaat = bestaat(records, new_record)

            if not record_bestaat:
                records.append(new_record)
            else:
                print('Record bestaat!')

            lineNr += 1

        return records


def print_kring_leden(records: list, kring: str):
    """
    Schrijf de gemaakte keuze voor een opgevraagde kring en de namen van de kringleden met de bijhorende code,naar een bestand resultaat-voorbeeld.txt.
    :param records:
    :return:
    """

    with open('resultaat-voorbeeld.txt', 'w+') as out_file:
        out_file.write(f'Kring: {kring}\n')
        for record in records:
            if record['Kring'] == kring:
                out_file.write(f'{record["Naam"]} - {record["Code"]}\n')


def aantal_leden_per_kring(records):
    leden = dict()

    for record in records:
        kring = record['Kring']
        if kring in leden:
            leden[kring] += 1
        else:
            leden[kring] = 1

    for (key, value) in leden.items():
        print(f'{key} {value}')


main()
