# Shared setup for Chapter 28. The chapter's blocks carry their own imports, so this file
# only makes sure the data file is in place.
# daily_revenue.csv is created by this chapter's Step 1, gen_daily.py. The blocks read it from the
# working directory exactly as the book does; if it is not here yet, use the copy shipped in
# data/generated/ (byte-identical to what the generator writes).
import os as _os, shutil as _shutil
if not _os.path.exists("daily_revenue.csv"):
    for _d in ("../../data/generated", "../data/generated", "data/generated"):
        if _os.path.exists(_os.path.join(_d, "daily_revenue.csv")):
            _shutil.copy(_os.path.join(_d, "daily_revenue.csv"), "daily_revenue.csv"); break
