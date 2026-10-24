def line_revenue(quantity, unit_price):
    """Revenue of one order line."""
    return float(quantity) * float(unit_price)

def invoice_total(rows):
    """Total revenue of the rows of one invoice (each row a dict of strings)."""
    return sum(line_revenue(r["Quantity"], r["UnitPrice"]) for r in rows)
