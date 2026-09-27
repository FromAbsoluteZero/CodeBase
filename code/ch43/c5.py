# Serving cost has its own tradeoff: batching several requests together
# raises throughput, since fixed per-batch overhead is shared across
# more predictions, but it raises the latency any single request in
# that batch has to wait for, since it waits for the whole batch to fill.
def simulate_serving(batch_size, per_batch_overhead_ms, per_item_ms,
                     arrival_rate_per_ms):
    # time to fill a batch, on average, given how fast requests arrive
    fill_time = batch_size / arrival_rate_per_ms
    compute_time = per_batch_overhead_ms + batch_size * per_item_ms
    # a request's expected wait: half the fill time (arrives at a random
    # point in the batch-filling window) plus the compute time
    avg_latency = fill_time / 2 + compute_time
    # predictions per second
    throughput = batch_size / (fill_time + compute_time) * 1000
    return avg_latency, throughput

print(f"{'batch size':>11}{'avg latency (ms)':>19}"
      f"{'throughput (pred/s)':>22}")
for batch in (1, 4, 8, 16, 32, 64):
    latency, throughput = simulate_serving(batch, per_batch_overhead_ms=8,
                                           per_item_ms=0.6,
                                           arrival_rate_per_ms=0.5)
    print(f"{batch:>11}{latency:>19.2f}{throughput:>22.1f}")

print(f"\nlarger batches serve far more predictions per second, at the cost")
print(f"of a slower response for any single one of them.")

# The latency above only holds if the server can keep up: it must clear a
# batch faster, on average, than requests arrive, or the queue never
# settles and grows without bound instead of leveling off near the number
# printed above. That condition is batch_size / compute_time > arrival_rate.
print(f"\n{'batch size':>11}{'utilization':>13}{'stable?':>10}")
for batch in (1, 4, 8, 16, 32, 64):
    compute_time = 8 + batch * 0.6
    # utilization = arrival_rate_per_ms / (batch_size / compute_time)
    utilization = 0.5 * compute_time / batch
    stable = "no" if utilization >= 1 else "yes"
    print(f"{batch:>11}{utilization:>13.2f}{stable:>10}")

print(f"\nbatch sizes one and four are unstable at this arrival rate: shown")
print(f"above for contrast, not as achievable latencies.")
