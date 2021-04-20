import csv

def parse_csv(csv_file):
    with open(csv_file) as file:
        reader = csv.DictReader(file)
        return list(reader)

