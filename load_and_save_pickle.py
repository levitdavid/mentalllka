import pickle

def load_pickle(file):
    try:
        with open(file, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден: {file}")
    except Exception as e:
        raise Exception(f"Ошибка загрузки pickle: {e}")

def save_pickle(table, file):
    try:
        with open(file, 'wb') as file:
            pickle.dump(table, file)
    except Exception as e:
        raise Exception(f"Ошибка сохранения pickle: {e}")
