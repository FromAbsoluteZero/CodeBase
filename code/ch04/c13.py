top = prod.index[0]
print(f"Revenue was ${clean['Revenue'].sum():,.0f} across "
      f"{clean['InvoiceNo'].nunique():,} invoices.")
print(f"The UK is {share.iloc[0]:.0f}% of it; the top two markets "
      f"are {share.iloc[:2].sum():.0f}%.")
print(f"H2 grew {(h2/h1-1):+.1%} on H1. {top} leads on revenue "
      f"at ${prod.loc[top,'revenue']:,.0f}.")
