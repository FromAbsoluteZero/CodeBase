A = np.arange(6).reshape(2, 3)
print("A", A.shape, "  A.T", A.T.shape)

# reshape: -1 means 'work it out'
v = np.arange(6)
print("as column", v.reshape(-1, 1).shape,
      " as row", v.reshape(1, -1).shape)

# a shape error, read as a sentence
try:
    A @ np.ones(2)
except ValueError as e:
    print("error:", str(e)[:58])

# broadcasting: this is the one that fails QUIETLY
X = np.arange(12).reshape(4, 3).astype(float)
col_means = X.mean(axis=0)          # shape (3,) - per feature
row_means = X.mean(axis=1)          # shape (4,) - per row
print("centered by column:", (X - col_means).shape, "correct")
print("centered by row:   ",
      (X - row_means.reshape(-1, 1)).shape, "also fine")
print("column means now:", (X - col_means).mean(axis=0).round(6))
