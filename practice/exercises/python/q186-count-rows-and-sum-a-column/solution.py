import csv

def row_count(path):
    """Number of data rows in the CSV at `path`."""
    with open(path, newline="") as f:
        return sum(1 for _ in csv.DictReader(f))

def total_quantity(path):
    """Sum of the Quantity column, as an int."""
    total = 0
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            total += int(row["Quantity"])
    return total
