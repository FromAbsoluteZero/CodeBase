import pandas as pd

def invoice_totals(df):
    """One row per InvoiceNo with its InvoiceTotal."""
    raise NotImplementedError

def add_invoice_total(df, totals=None):
    """The lines of df with InvoiceTotal attached (left merge, validate='m:1').
    `totals` defaults to invoice_totals(df); the check passes a bad one to see the merge refuse it."""
    raise NotImplementedError
