import csv
import os


def read_addresses(filename):

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        print('-' * 100)
        print('CSV file: ', filename)
        print('-' * 100)

        for row in reader:
            if reader.line_num == 1:
                print(
                    '{:10s} {:18} {:20s} {:14s} {:10s} {:}'.format(
                        row[0], row[1], row[1], row[3], row[4], row[5]
                    )
                )
                print('-' * 100)
            else:
                print(
                    '{:12s} {:12s} {:22s} {:18s} {:11s} {:}'.format(
                        row[0], row[1], row[2], row[3], row[4], row[5]
                    )
                )

    return '...Done'


csv_file = os.path.join(os.path.dirname(__file__), 'addresses.csv')
print(read_addresses(csv_file))
