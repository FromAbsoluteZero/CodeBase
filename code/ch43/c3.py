# The trap: concept drift changes the relationship between features and
# the outcome, not the features themselves. A monitor watching only the
# input distribution can see nothing wrong at all while the model
# quietly degrades to worse than chance.
r2 = np.random.default_rng(430)

def make_labels(x, true_boundary):
    return (x > true_boundary).astype(int)

x_train = r2.normal(50, 10, 2000)
y_train = make_labels(x_train, true_boundary=50)     # trained decision boundary: x > 50

# a simple threshold "model", fit once at training time and never touched again
model_boundary = 50.0

print(f"{'week':>6}{'feature mean':>14}{'feature KS p-value':>20}{'true boundary':>15}{'model accuracy':>16}")
for week in range(0, 13):
    x_live = r2.normal(50, 10, 500)                   # feature distribution: UNCHANGED, every week
    true_boundary_now = 50 + week * 2.5               # but what defines the outcome keeps moving
    y_live = make_labels(x_live, true_boundary_now)
    pred = (x_live > model_boundary).astype(int)
    acc = (pred == y_live).mean()
    _, p = ks_test(x_train, x_live)
    print(f"{week:>6}{x_live.mean():>14.2f}{p:>20.4f}{true_boundary_now:>15.1f}{acc:>16.4f}")

print(f"\nthe feature distribution never moves, so every distribution-based")
print(f"monitor in Steps 1 and 2 would report perfect stability every week.")
