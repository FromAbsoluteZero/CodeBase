# A common fix: use a different approval threshold per group so that
# false-positive rates match exactly. This is a real, deployable
# intervention. What it costs is calibration: the same predicted score
# now means something different depending on which group a person is in.
def fpr_at_threshold(p, y_true, group_mask, threshold):
    pred_t = (p >= threshold).astype(int)
    y_t, y_p = y_true[group_mask], pred_t[group_mask]
    return y_p[y_t == 0].mean()

target_fpr = fpr_at_threshold(p_repay, y, group == 1, 0.5)   # match group 1's original FPR

best_thresh, best_gap = 0.5, 1.0
for t in np.linspace(0.01, 0.99, 400):
    f = fpr_at_threshold(p_repay, y, group == 0, t)
    gap = abs(f - target_fpr)
    if gap < best_gap:
        best_gap, best_thresh = gap, t

pred_equalized = pred.copy()
pred_equalized[group == 0] = (p_repay[group == 0] >= best_thresh).astype(int)

tpr0_eq, fpr0_eq = group_rates(y, pred_equalized, group == 0)
tpr1_eq, fpr1_eq = group_rates(y, pred_equalized, group == 1)

print(f"to match group 1's false-positive rate of {target_fpr:.4f}, group 0's")
print(f"approval threshold must move from 0.500 to {best_thresh:.3f}")
print(f"\n{'group':>8}{'threshold':>12}{'FPR':>10}{'TPR':>10}{'approval rate':>16}")
print(f"{'0':>8}{best_thresh:>12.3f}{fpr0_eq:>10.4f}{tpr0_eq:>10.4f}"
      f"{pred_equalized[group==0].mean():>16.4f}")
print(f"{'1':>8}{0.5:>12.3f}{fpr1_eq:>10.4f}{tpr1_eq:>10.4f}"
      f"{pred_equalized[group==1].mean():>16.4f}")

print(f"\nFPR now matches almost exactly. But a person in group 0 with a")
print(f"predicted repayment probability of {best_thresh:.2f} is now REJECTED,")
print(f"while a person in group 1 with the identical predicted probability")
print(f"of {best_thresh:.2f} is APPROVED, at the unchanged threshold of 0.5.")
print(f"the same score now means two different decisions.")
