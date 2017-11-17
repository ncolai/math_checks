from scipy.stats import uniform, norm
import matplotlib.pyplot as plt
import numpy as np

def hist_sums(dist):
    samples = np.array([int(dist.rvs(size=100).sum()) for i in range(100000)])
    range_counts = {i:0.000 for i in range(30,61)}
    unique,counts = np.unique(samples, return_counts = True)
    for u,c in zip(unique,counts):
        if u in range_counts:
            range_counts[u] = float("{:.3f}".format(c/float(100000)))
    print(zip(range_counts.keys(), range_counts.values()))
    plt.bar(range_counts.keys(), range_counts.values(), 1, color='g')
    plt.show()

if __name__ == "__main__":
    hist_sums(uniform(0,1))
    approx = norm(50, (float(100)/12) ** 0.5)
    print(approx.cdf(48.5) - approx.cdf(47.5))

