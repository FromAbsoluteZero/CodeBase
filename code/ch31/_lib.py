import numpy as np, warnings; warnings.filterwarnings("ignore")
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

digits = load_digits()
X, y = digits.data / 16.0, digits.target
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2,
                                      stratify=y, random_state=0)

def softmax(z):
    z = z - z.max(axis=-1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=-1, keepdims=True)

def naive_init(sizes, seed):
    r = np.random.default_rng(seed)
    return [r.normal(0, 1, (sizes[i], sizes[i+1])) for i in range(len(sizes)-1)]

def he_init(sizes, seed):
    r = np.random.default_rng(seed)
    return [r.normal(0, np.sqrt(2 / sizes[i]), (sizes[i], sizes[i+1]))
            for i in range(len(sizes) - 1)]

deep_sizes = [64, 64, 64, 64, 64, 10]      # five weight layers, shared by every demo
