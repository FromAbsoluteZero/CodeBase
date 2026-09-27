import csv

def missing_customer_ids(path):
    """(number of rows with an empty CustomerID, that number as a share of all rows)."""
    total = missing = 0
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            total += 1
            if row["CustomerID"].strip() == "":
                missing += 1
    return missing, missing / total
