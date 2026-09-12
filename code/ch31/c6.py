# The BN implementation above never updates gamma and beta: computing
# their gradients requires differentiating through the normalization
# itself, since the mean and variance both depend on every example in
# the batch. That is real, non-trivial calculus, and it is exactly the
# work automatic differentiation exists to do for you.
#
# What can be checked without it: does the fix from Step 5 depend on
# which naive initialization was unlucky, or is it reliable?
print(f"{'seed':>6}{'no BN, final acc':>18}{'with BN, final acc':>20}")
for seed in (10, 11, 12, 13):
    h1 = train(deep_sizes, naive_init, seed=seed, eta=0.05, epochs=250)
    h2 = train_bn(deep_sizes, naive_init, seed=seed, eta=0.05, epochs=250)
    print(f"{seed:>6}{h1[-1][2]:>18.4f}{h2[-1][2]:>20.4f}")
