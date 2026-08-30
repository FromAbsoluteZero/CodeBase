# A controlled setting: a large pretrained weight matrix, of the kind a
# transformer's attention or feedforward projection actually uses, and
# a target task whose correct adaptation is, by construction, a
# low-rank change. This lets the low-rank hypothesis behind LoRA be
# checked directly rather than only argued for.
r = np.random.default_rng(39)
D = 256                                   # a modest transformer-layer width
W_pretrained = r.normal(0, np.sqrt(1/D), (D, D))

true_rank = 4
A_true = r.normal(0, 0.5, (D, true_rank))
B_true = r.normal(0, 0.5, (true_rank, D))
W_target_true = W_pretrained + A_true @ B_true      # the update the target task actually needs

full_params = W_pretrained.size
lora_params = D * true_rank + true_rank * D

print(f"pretrained weight matrix:      {W_pretrained.shape}   {full_params:,} parameters")
print(f"true adaptation needed:       rank {true_rank}")
print(f"full fine-tuning would train: {full_params:,} parameters")
print(f"LoRA at rank {true_rank} would train:  {lora_params:,} parameters "
      f"({100*lora_params/full_params:.2f}% of full)")
print(f"that is a {full_params/lora_params:.0f}x reduction in trainable parameters")
