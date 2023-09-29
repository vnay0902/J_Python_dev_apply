import csv

class CSVORM:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.csv_file, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                data = list(reader)
            return data
        except FileNotFoundError:
            return []

    def list(self):
        return self.data

    def get(self, id):
        for row in self.data:
            if row.get('ID') == id:
                return row
        return None

    def filter(self, column_name, value):
        filtered_data = [row for row in self.data if row.get(column_name) == value]
        return filtered_data

# Example usage:
if __name__ == "__main__":
    csv_file_path = "data.csv"  # Replace with your CSV file path

    # Initialize the ORM with the CSV file
    orm = CSVORM(csv_file_path)

    # List all rows
    all_rows = orm.list()
    print("All Rows:")
    for row in all_rows:
        print(row)

    # Get a specific row by ID
    id_to_get = "1"
    specific_row = orm.get(id_to_get)
    print("\nRow with ID =", id_to_get)
    print(specific_row)

    # Filter rows by a specific column and value
    column_to_filter = "Age"  # Replace with the desired column name
    value_to_filter = "30"    # Replace with the desired value
    filtered_rows = orm.filter(column_to_filter, value_to_filter)
    print(f"\nRows where {column_to_filter} = {value_to_filter}:")
    for row in filtered_rows:
        print(row)

