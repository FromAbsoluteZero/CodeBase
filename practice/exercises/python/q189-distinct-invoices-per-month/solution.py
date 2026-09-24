import csv

def invoices_per_month(path):
    """{'YYYY-MM': number of distinct InvoiceNo values in that month}."""
    seen = {}
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            month = row["InvoiceDate"][:7]
            seen.setdefault(month, set()).add(row["InvoiceNo"])
    return {month: len(invoices) for month, invoices in sorted(seen.items())}
