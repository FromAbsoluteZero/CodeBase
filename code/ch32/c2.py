# Why convolution instead of a fully connected layer: parameter count,
# and what each parameter is even allowed to depend on.
img_size = 8 * 8                       # this dataset
n_filters, k = 4, 3

fc_params = img_size * 32              # a modest 32-unit hidden layer
conv_params = n_filters * (k * k)      # four 3x3 filters, weights only

print(f"{'architecture':<28}{'parameters':>12}")
print(f"{'fully connected, 32 hidden':<28}{fc_params:>12,}")
print(f"{'conv, 4 filters of 3x3':<28}{conv_params:>12,}")
print(f"ratio: {fc_params / conv_params:.0f}x fewer parameters in the conv layer")

for side in (8, 32, 256):
    n = side * side
    print(f"\nat a {side}x{side} image:")
    print(f"  fully connected, 32 hidden: {n*32:>10,} parameters")
    print(f"  conv, 4 filters of 3x3:     {conv_params:>10,} parameters  (unchanged)")
