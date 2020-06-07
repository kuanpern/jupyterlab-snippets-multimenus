x = np.random.randn(10000)  # example data, random normal distribution
num_bins = 50
n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor="green", alpha=0.5)
plt.xlabel(r"Description of $x$ coordinate (units)")
plt.ylabel(r"Description of $y$ coordinate (units)")
plt.title(r"Histogram title here (remove for papers)")
plt.show();