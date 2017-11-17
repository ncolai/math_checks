import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def load_input():
    data = np.genfromtxt('peerGrades.csv')
    #overall mean of sample
    print(sum(data)/len(data))
    return data

def sample_mean_median(data):
    means, medians = [],[]

    #take samples and find stats of each
    for i in range(10000):
        sample = np.random.choice(data, 5)
        sample.sort()
        means.append(sum(sample)/len(sample))
        medians.append(sample[2])

    #calculate statistics for samples overall
    for arr in means, medians:
        arr_mean = sum(arr)/len(arr)
        var_arr = [(i - arr_mean)**2 for i in arr]
        #print sample mean, sample variance
        print(arr_mean, sum(var_arr)/len(var_arr))
        #plot both
        plt.figure()
        plt.hist(means, alpha=1)
        plt.figure()
        plt.hist(medians, alpha=1)
        plt.show()

if __name__ == "__main__":
    my_data = load_input()
    sample_mean_median(my_data)
