import csv

def to_float(text, default=None):
    """float(text), or `default` when text is empty or not a number."""
    try:
        return float(text)
    except (TypeError, ValueError):
        return default

def mean_invoice_total(path):
    """Mean revenue of the non-cancelled invoices."""
    totals = {}
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            if row["InvoiceNo"].startswith("C"):
                continue
            revenue = to_float(row["Quantity"], 0.0) * to_float(row["UnitPrice"], 0.0)
            totals[row["InvoiceNo"]] = totals.get(row["InvoiceNo"], 0.0) + revenue
    return sum(totals.values()) / len(totals)
