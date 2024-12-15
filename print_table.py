def print_table(self):
    try:
        print(" | ".join(self.header))
        for row in self.data:
            print(" | ".join(map(str, row))) 
    except Exception as e:
        raise Exception(f"Error in print_table: {e}")
