import csv

def _counts(path):
    counts = {}
    with open(path, newline="") as f:
        reader = csv.reader(f)
        next(reader)  # header
        for row in reader:
            key = tuple(row)
            counts[key] = counts.get(key, 0) + 1
    return counts

def duplicate_rows(path):
    """Distinct rows (as tuples) that appear more than once, in order of first appearance."""
    return [row for row, n in _counts(path).items() if n > 1]

def extra_copies(path):
    """Number of rows beyond the first copy of each duplicated row."""
    return sum(n - 1 for n in _counts(path).values() if n > 1)
