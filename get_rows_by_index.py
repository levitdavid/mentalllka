def get_rows_by_index(self, *values, copy_table=False):
    try:
        if not values:
            raise ValueError("Не указаны значения для поиска.")
        rows = [row for row in self.data if row[0] in values]
        if not rows:
            raise ValueError("Ни одна строка не соответствует указанным значениям.")
        if copy_table:
            return TableData(self.header, [row[:] for row in rows])
        return TableData(self.header, rows)
    except ValueError as e:
        raise ValueError(f"Ошибка в get_rows_by_index: {e}")
    except Exception as e:
        raise Exception(f"Ошибка в get_rows_by_index: {e}")
