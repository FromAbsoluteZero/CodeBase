import math
import pandas as pd

def overtime_effect(df):
    """Rates, difference, 95% interval and p-value, as described in README.md."""
    yes = df.loc[df["OverTime"] == "Yes", "Attrition"]
    no = df.loc[df["OverTime"] == "No", "Attrition"]
    p1, p2, n1, n2 = yes.mean(), no.mean(), len(yes), len(no)
    diff = p1 - p2
    se = math.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
    pooled = (yes.sum() + no.sum()) / (n1 + n2)
    se_pooled = math.sqrt(pooled * (1 - pooled) * (1 / n1 + 1 / n2))
    z = diff / se_pooled
    p_value = 2 * (1 - 0.5 * (1 + math.erf(abs(z) / math.sqrt(2))))
    return {
        "rate_overtime": float(p1), "rate_no_overtime": float(p2), "difference": float(diff),
        "ci_low": float(diff - 1.96 * se), "ci_high": float(diff + 1.96 * se),
        "p_value": float(p_value),
    }
