import numpy as np, warnings, re; warnings.filterwarnings("ignore")
from collections import Counter, defaultdict

def make_corpus(n_docs, seed):
    """Synthetic customer-review-style text from a hand-built grammar with
    realistic word frequencies (Zipfian), so tokenization, decoding, and
    scaling can be demonstrated on text with no copyright status question."""
    r = np.random.default_rng(seed)
    subjects = ["the product", "this item", "the device", "the service", "delivery",
                "the packaging", "the battery", "the screen", "support", "the app"]
    verbs = ["arrived", "worked", "broke", "improved", "failed", "lasted",
             "shipped", "performed", "exceeded", "disappointed"]
    adverbs = ["quickly", "slowly", "eventually", "immediately", "barely",
               "consistently", "rarely", "surprisingly", "finally", "never"]
    objects = ["expectations", "the first week", "two days", "a month",
               "the warranty period", "every test", "the price point",
               "my needs", "the description", "the competition"]
    connectors = ["and", "but", "so", "because", "although", "while"]

    def weighted(options, alpha=1.3):
        w = np.array([1 / (i + 1) ** alpha for i in range(len(options))])
        return r.choice(options, p=w / w.sum())

    docs = []
    for _ in range(n_docs):
        n_sent = r.integers(1, 4)
        sentences = []
        for _ in range(n_sent):
            s = f"{weighted(subjects)} {weighted(verbs)} {weighted(adverbs)}"
            if r.random() < 0.6:
                s += f" {weighted(connectors)} {weighted(subjects)} {weighted(verbs)} {weighted(objects)}"
            sentences.append(s)
        docs.append(". ".join(sentences) + ".")
    return docs
