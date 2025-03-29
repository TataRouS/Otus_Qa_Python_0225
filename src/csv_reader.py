import csv


def read_csv(filename):
    result = []
    with open(filename, newline="") as f:
        reader = csv.reader(f)

        # Извлекаем заголовок
        header = next(reader)

        # Итерируется по данным делая из них словари
        for row in reader:
            result.append(dict(zip(header, row)))
    return result
