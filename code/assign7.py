from scipy.stats import binom

x=binom.pmf(2,7,1/6)

print("Required probability is {0:.3f}".format(x))
