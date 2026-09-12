print(f"1. Calling the 60 highest-scoring employees finds "
      f"{caught} of {yte.sum()} leavers, versus {rand:.0f} at random.")
print(f"2. Precision is {caught/budget:.0%}, so two in three calls "
      f"reach someone who was staying.")
print(f"3. That clears the {call_cost/(replace_cost*success):.0%} "
      f"break-even precision comfortably.")
print(f"4. Net value ${caught*success*replace_cost - budget*call_cost:,.0f} "
      f"depends entirely on the unmeasured {success:.0%} save rate.")
ot = X.columns.get_loc('OverTime_Yes')
odds_ratio = np.exp(model.coef_[0] / sc.scale_)[ot]
print(f"5. Overtime multiplies the odds of leaving by {odds_ratio:.1f} "
      f"- worth a policy conversation, not just calls.")
