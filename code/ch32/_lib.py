import numpy as np, warnings; warnings.filterwarnings("ignore")
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

digits = load_digits()
X_img = digits.images / 16.0            # (n, 8, 8), unflattened
X, y = digits.data / 16.0, digits.target
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2,
                                      stratify=y, random_state=0)
Xtr_img, Xte_img = Xtr.reshape(-1, 8, 8), Xte.reshape(-1, 8, 8)

def softmax(z):
    z = z - z.max(axis=-1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=-1, keepdims=True)
