"""

Variance is in the scale of the data.

The "raw" variance value may be difficult to interpret.

Look for large differences in variances across variables.

High variance increases risk of statistical flukes or unreliable results.

Z-scoring or other normalizations may be appropriate.
"""

import statistics

data = [2, 3, 4, 3, 4, 4]

# Sample variance
variance = statistics.variance(data)
print("Variance:", variance)


# Population variance
pop_variance = statistics.pvariance(data)

# Population standard deviation
pop_std_dev = statistics.pstdev(data)

print("Population Variance:", pop_variance)
print("Population Standard Deviation:", pop_std_dev)