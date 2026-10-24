prior = 0.06     # P(churn)
recall = 0.70    # P(flag | churn)
fpr = 0.15       # P(flag | no churn)
offer = 6.00
value = 180.00

print(f"P(flag | churn)    = {recall:.2f}  <- conditions on CHURN")
print(f"P(flag | no churn) = {fpr:.2f}  <- conditions on NO CHURN")
print(f"P(churn)           = {prior:.2f}  <- the base rate")
