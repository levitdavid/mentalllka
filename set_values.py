def set_values(self, values, column=0):
    try:
        col_index = column if isinstance(column, int) else self.header.index(column)
        if len(values) != len(self.data):
            raise ValueError("Длина значений не соответствует количеству строк.")
        for i, value in enumerate(values):
            self.data[i][col_index] = value
    except Exception as e:
        raise Exception(f"Ошибка в set_values: {e}")
