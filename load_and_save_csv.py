import csv
def load_csv(file):
    try:
        with open(file, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)
            data = list(reader)
            return TableData(header, data)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден: {file}")
    except Exception as e:
        raise Exception(f"Ошибка загрузки CSV: {e}")

def save_csv(table, file):
    try:
        with open(file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(table.header)
            writer.writerows(table.data)
    except Exception as e:
        raise Exception(f"Ошибка сохрания CSV: {e}")
