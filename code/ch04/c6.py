pv = m.pivot_table(index="Region", columns="Category",
                   values="Revenue", aggfunc="sum").round(0)
print(pv.to_string())

# and back to long form
long = pv.reset_index().melt(id_vars="Region",
                             value_name="Revenue")
print(long.head(4).to_string(index=False))
