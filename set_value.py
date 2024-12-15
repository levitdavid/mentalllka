def set_value(self, value, column=0):
    try:
        if len(self.data) != 1:
            raise ValueError("Таблица содержит более одной строки.")
        col_index = column if isinstance(column, int) else self.header.index(column)
        self.data[0][col_index] = value
    except Exception as e:
        raise Exception(f"Ошибка в set_value: {e}")
