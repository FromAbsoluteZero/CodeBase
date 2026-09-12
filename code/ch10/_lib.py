# Shared setup for Chapter 10. The chapter's blocks carry their own imports, so this file
# only makes sure the data file is in place.
# retail.csv is created by Chapter 4 (code/ch04/gen_retail.py). The blocks read it from the
# working directory exactly as the book does; if it is not here yet, use the copy shipped in
# data/generated/ (byte-identical to what the generator writes).
import os as _os, shutil as _shutil
if not _os.path.exists("retail.csv"):
    for _d in ("../../data/generated", "../data/generated", "data/generated"):
        if _os.path.exists(_os.path.join(_d, "retail.csv")):
            _shutil.copy(_os.path.join(_d, "retail.csv"), "retail.csv"); break
