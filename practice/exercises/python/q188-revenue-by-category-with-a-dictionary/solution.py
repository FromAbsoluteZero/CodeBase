import csv

def revenue_by_category(path):
    """{category: total revenue} for the CSV at `path`."""
    totals = {}
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            revenue = float(row["Quantity"]) * float(row["UnitPrice"])
            totals[row["Category"]] = totals.get(row["Category"], 0.0) + revenue
    return totals
