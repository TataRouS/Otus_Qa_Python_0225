import csv

# import DictRreader
from files import CSV_FILE_PATH

with open(CSV_FILE_PATH, newline="") as f:
    reader = csv.reader(f)

    # Извлекаем заголовок
    header = next(reader)

    # Итерируется по данным делая из них словари
    for row in reader:
        print(dict(zip(header, row)))

# with open(CSV_FILE_PATH, newline='') as f:
#   reader = DictReader(f)
##Итерируется по данным делая из них словари
# for row in reader:
# prin(row)
