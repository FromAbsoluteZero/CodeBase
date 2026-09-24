import csv

def lines_per_invoice(path):
    """{InvoiceNo: number of order lines}."""
    counts = {}
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            counts[row["InvoiceNo"]] = counts.get(row["InvoiceNo"], 0) + 1
    return counts

def invoices_with_more_than(path, k):
    """Number of invoices with more than k lines."""
    return sum(1 for n in lines_per_invoice(path).values() if n > k)
