def main():
    try:
        records = leesInput('test3-voorbeeld2.txt')

        kring = input('Van welke kring wil je de leden afdrukken?')
        print(f'Je hebt gekozen voor {kring}!')
        print_kring_leden(records, kring)
        aantal_leden_per_kring(records)

    except Exception as e:
        print(e)
        print('Zorg voor de juiste input!')


def leesInput(filename):
    with open(filename, 'r') as input_file:
        veldnamen = input_file.readline().rstrip('\n')
        veldnamen = veldnamen.split(';')

        records = set()

        lineNr = 2
        for line in input_file.readlines():
            line = line.rstrip('\n')

            record_elements = tuple(line.split(';'))

            if len(record_elements) != len(veldnamen):
                raise Exception(
                    f'Lijn {lineNr}: aantal veldnamen moet {len(veldnamen)} zijn, maar is {len(record_elements)}')

            records.add(record_elements)

            lineNr += 1

        return records


def print_kring_leden(records, kring):
    with open('resultaat-voorbeeld.txt', 'w+') as out_file:
        out_file.write(f'Kring: {kring}\n')
        for record in records:
            if record[2] == kring:
                out_file.write(f'{record[0]} - {record[1]}\n')


def aantal_leden_per_kring(records):
    leden = dict()

    for record in records:
        kring = record[2]
        if kring in leden:
            leden[kring] += 1
        else:
            leden[kring] = 1

    for (key, value) in leden.items():
        print(f'{key} {value}')


main()
