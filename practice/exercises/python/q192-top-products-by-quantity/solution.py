import csv

def top_products(path, n):
    """The n products with the largest total Quantity, as (Description, total) tuples, largest first."""
    totals = {}
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            totals[row["Description"]] = totals.get(row["Description"], 0) + int(row["Quantity"])
    ranked = sorted(totals.items(), key=lambda kv: (-kv[1], kv[0]))
    return ranked[:n]
