# A toy judge, built to be simple enough to inspect completely: it
# scores a response by a mix of length and vocabulary overlap with the
# question, then picks a winner between two candidates. This is not a
# language model. It is simple enough that its own biases can be shown
# in full, which is the point: the same class of bias is documented in
# real LLM judges by the papers cited at the end of this chapter, and
# a fully transparent toy version makes the mechanism visible rather
# than asserted.
def toy_judge_score(response, question_words):
    words = response.lower().split()
    overlap = len(set(words) & question_words)
    length_bonus = len(words) * 0.15                  # the deliberate flaw: rewards length
    return overlap + length_bonus

def toy_judge_compare(resp_a, resp_b, question):
    qwords = set(question.lower().split())
    score_a = toy_judge_score(resp_a, qwords)
    score_b = toy_judge_score(resp_b, qwords)
    return "A" if score_a > score_b else "B"

question = "what causes the seasons to change on Earth"
short_correct = "Earth's tilted axis changes how directly sunlight hits each hemisphere through the year."
long_padded = ("Well, that's a great question, and there are actually many interesting factors to " +
              "consider here, but if we think about it carefully and look at the science, the main " +
              "thing going on is really about how Earth's axis is tilted relative to its orbit.")

winner_1 = toy_judge_compare(short_correct, long_padded, question)
winner_2 = toy_judge_compare(long_padded, short_correct, question)     # same pair, order swapped

print(f"short, correct answer:  {len(short_correct.split())} words")
print(f"long, padded answer:    {len(long_padded.split())} words, same core claim, wrapped in filler")
print(f"\npresented as (A=short, B=long): judge prefers {winner_1}")
print(f"presented as (A=long, B=short): judge prefers {winner_2}")
