# A transparent toy router: it picks a tool by keyword match against a
# task description. Simple enough to see exactly how it can fail, which
# is the point: real tool-routing failures in production agents look
# structurally like this, even when the router itself is a full model.
TOOLS = {
    "calculator": {"total", "average", "percent"},
    "search": {"who", "when", "where"},
    "code_exec": {"run", "debug"},
    "database": {"table", "customer"},
}

def route(words, confusion_prob, r):
    """With probability confusion_prob, add one keyword from a
    DIFFERENT tool into the task's own words, simulating a genuinely
    ambiguous or poorly-phrased sub-task description that legitimately
    points two ways at once."""
    words = set(words)
    if r.random() < confusion_prob:
        other_tool = r.choice([t for t in TOOLS if t not in
                               [tt for tt in TOOLS if words & TOOLS[tt]]] or list(TOOLS))
        words.add(r.choice(list(TOOLS[other_tool])))
    scores = {tool: len(words & kws) for tool, kws in TOOLS.items()}
    best = max(scores.values())
    tied = [t for t, s in scores.items() if s == best]
    return r.choice(tied)                              # ties broken at random, honestly

# each task has exactly ONE clean keyword: borderline by construction
tasks = [
    (["find", "the", "total", "for", "last", "month"], "calculator"),
    (["find", "who", "founded", "the", "company"], "search"),
    (["please", "run", "the", "validation", "job"], "code_exec"),
    (["look", "at", "the", "customer", "records"], "database"),
]

print(f"{'confusion rate':>15}{'per-call routing accuracy':>27}")
for confusion in (0.0, 0.15, 0.30, 0.50, 0.70):
    r = np.random.default_rng(41)
    correct, n_trials = 0, 4000
    for i in range(n_trials):
        words, true_tool = tasks[i % len(tasks)]
        picked = route(words, confusion, r)
        correct += (picked == true_tool)
    print(f"{confusion:>15.2f}{correct/n_trials:>27.4f}")
