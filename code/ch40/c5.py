# The standard mitigation for position bias costs exactly double the
# judging calls: present the same pair in both orders, and treat a
# disagreement between the two runs as "no clear winner" rather than
# trusting whichever order happened to be used.
def debiased_compare(resp_a, resp_b, question):
    verdict_1 = biased_judge_compare(resp_a, resp_b, question)
    verdict_2 = biased_judge_compare(resp_b, resp_a, question)
    winner_1 = resp_a if verdict_1 == "A" else resp_b
    winner_2 = resp_b if verdict_2 == "A" else resp_a
    if winner_1 == winner_2:
        return winner_1, True                          # both orders agree: a real signal
    return None, False                                  # disagreement: flag it, don't guess

resolved, flagged = 0, 0
for _ in range(200):
    len_a = r_bias.integers(10, 15)
    len_b = r_bias.integers(10, 15)
    fake_a = " ".join(["word"] * len_a)
    fake_b = " ".join(["word"] * len_b)
    winner, agreed = debiased_compare(fake_a, fake_b, question)
    if agreed:
        resolved += 1
    else:
        flagged += 1

print(f"of the same 200 near-tied pairs, checking both orders:")
print(f"  agreed on a genuine winner: {resolved}")
print(f"  flagged as no clear winner (orders disagreed): {flagged}")
print(f"\nthe single-order judge from Step 4 confidently declared a winner")
print(f"in all 200 cases, 157 of them driven purely by position. Checking")
print(f"both orders converts most of that false confidence into an honest")
print(f"'no clear winner,' at twice the cost in judging calls.")
