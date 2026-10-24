print(f"Flagging catches {tp/churners:.0%} of churners but only "
      f"{tp/(tp+fp):.0%} of flags are real churners.")
print(f"The campaign pays if the offer persuades more than "
      f"{breakeven:.1%} of at-risk customers to stay.")
print("Nobody has measured that rate. Measure it with a randomized test:")
print("assign flagged customers at random to the offer or to a control")
print("group, fix both sizes in advance to detect a persuasion rate that")
print("would change the decision (Chapter 15 shows how), and read the")
print("result once that planned sample and follow-up are complete.")
