from sklearn.inspection import partial_dependence

for feat in ["YearsAtCompany", "JobSatisfaction"]:
    pd_ = partial_dependence(rf, Xte, [list(X.columns).index(feat)],
                             kind="average", grid_resolution=6)
    grid = pd_["grid_values"][0]
    vals = pd_["average"][0]
    print(f"{feat}")
    for g, v in zip(grid, vals):
        print(f"   {g:>6.1f}  ->  predicted attrition {v:.3f}")
