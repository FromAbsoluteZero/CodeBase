print(f"Flagging catches {tp/churners:.0%} of churners but only "
      f"{tp/(tp+fp):.0%} of flags are real churners.")
print(f"The campaign pays if the offer persuades more than "
      f"{breakeven:.1%} of at-risk customers to stay.")
print(f"Nobody has measured that rate. Hold back 10% of "
      f"flagged customers as a control and we will know in a quarter.")
