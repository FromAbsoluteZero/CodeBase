# Demographic parity is only one definition of fairness. Equalized odds
# asks a different question: among people who would actually repay, is
# the model equally likely to approve them, regardless of group? And
# among people who would default, is it equally likely to correctly
# reject them?
def group_rates(y_true, y_pred, group_mask):
    y_t, y_p = y_true[group_mask], y_pred[group_mask]
    tpr = y_p[y_t == 1].mean()          # true positive rate: approved among true repayers
    fpr = y_p[y_t == 0].mean()          # false positive rate: approved among true defaulters
    return tpr, fpr

tpr0, fpr0 = group_rates(y, pred, group == 0)
tpr1, fpr1 = group_rates(y, pred, group == 1)

print(f"{'group':>8}{'TPR (approve true repayers)':>30}{'FPR (approve true defaulters)':>32}")
print(f"{'0':>8}{tpr0:>30.4f}{fpr0:>32.4f}")
print(f"{'1':>8}{tpr1:>30.4f}{fpr1:>32.4f}")
print(f"\nTPR gap: {abs(tpr0-tpr1):.4f}    FPR gap: {abs(fpr0-fpr1):.4f}")

# calibration: among people the model scores at a given confidence
# level, does that confidence mean the same thing in both groups?
print(f"\n{'score bucket':>14}{'group 0 actual repay rate':>27}{'group 1 actual repay rate':>27}")
for lo, hi in [(0.4, 0.5), (0.5, 0.6), (0.6, 0.7), (0.7, 0.8)]:
    mask = (p_repay >= lo) & (p_repay < hi)
    r0 = y[(group == 0) & mask].mean() if (mask & (group==0)).sum() > 0 else float('nan')
    r1 = y[(group == 1) & mask].mean() if (mask & (group==1)).sum() > 0 else float('nan')
    print(f"{f'{lo}-{hi}':>14}{r0:>27.4f}{r1:>27.4f}")
