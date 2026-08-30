# Position bias is a different failure from length bias: even holding
# content fixed, a judge can favour whichever answer sits in a
# particular slot. This toy judge scores both responses identically on
# content and adds a small, fixed preference for whichever is shown
# first, exactly the kind of subtle artifact documented in real judge
# models trained on data where the first option happened to be
# correct slightly more often.
def biased_judge_compare(resp_a, resp_b, question, position_bonus=0.4):
    qwords = set(question.lower().split())
    score_a = toy_judge_score(resp_a, qwords) + position_bonus   # "shown first" bonus
    score_b = toy_judge_score(resp_b, qwords)
    return "A" if score_a > score_b else "B"

resp_1 = "The seasonal cycle is driven by the tilt of Earth's rotational axis."
resp_2 = "Earth's axial tilt changes the angle of incoming sunlight across the year."

print("two responses of near-identical length and content:")
print(f"  resp_1: {len(resp_1.split())} words")
print(f"  resp_2: {len(resp_2.split())} words")

win_a_first = biased_judge_compare(resp_1, resp_2, question)
win_b_first = biased_judge_compare(resp_2, resp_1, question)
print(f"\nshown as (A=resp_1, B=resp_2): judge picks {win_a_first}")
print(f"shown as (A=resp_2, B=resp_1): judge picks {win_b_first}")
print(f"\nthe judge picked whichever response was shown in slot A both times,")
print(f"despite the two responses being interchangeable in content and length.")

# quantify how often this happens across many near-tied response pairs
r_bias = np.random.default_rng(40)
flips = 0
for _ in range(200):
    len_a = r_bias.integers(10, 15)
    len_b = r_bias.integers(10, 15)
    fake_a = " ".join(["word"] * len_a)
    fake_b = " ".join(["word"] * len_b)
    w1 = biased_judge_compare(fake_a, fake_b, question)
    w2 = biased_judge_compare(fake_b, fake_a, question)
    # a consistent judge would pick the SAME underlying response both times;
    # this judge picks "A" both times, i.e. whichever is shown first
    if w1 == "A" and w2 == "A":
        flips += 1
print(f"\nacross 200 near-tied pairs, the judge preferred slot A regardless")
print(f"of content in {flips} of 200 cases ({100*flips/200:.0f}%).")
