from math import comb

n, p = 20, 0.25          # 20 leads, each converts 25% of the time

def binom(k):
    return comb(n, k) * p**k * (1 - p)**(n - k)

print(f"expected conversions: {n * p:.1f}")
print(f"standard deviation:   {(n * p * (1 - p))**0.5:.2f}")
print()
for k in [0, 3, 5, 8]:
    print(f"  P(exactly {k}) = {binom(k):.4f}")

at_least_8 = sum(binom(k) for k in range(8, n + 1))
print(f"\nP(at least 8) = {at_least_8:.4f}")
