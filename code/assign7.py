from scipy.stats import binom

x=binom.pmf(2,7,1/6)

print("Theoretical probability is 0.2344. Practical probability is {0:.3f}".format(x))
