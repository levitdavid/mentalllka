def get_rows_by_number (self, start, stop=None, copy_table=False):
    try:
      if stop is None:
          stop = start + 1
      rows = self.data [start: stop]
      if copy_table:
          return TableData(self.header, [row[:] for row in rows])
      return TableData(self.header, rows)
except IndexError:
    raise IndexError("Указан неверный диапазон индексов строк.")
except Exception as e:
    raise Exception(f"Ошибка в get_rows_by_number: {e}")
