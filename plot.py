from matplotlib import pyplot as plt
import numpy as np
from numba import njit, prange, jit
plt.style.use('seaborn')



def main():
    scores = np.load("scores_mult.npy")

    bins = np.array([0.0, 10.0, np.inf])
    max_step = 3000

    linewidth = 1.5
    hist, hist_means = get_histograms(scores, max_step, bins)
    print(hist_means)
    plt.plot(np.log10(hist_means.T[1]), linestyle = "--", linewidth=linewidth)
    plt.plot(np.log10(hist_means.T[0]), linestyle = ":", linewidth=linewidth)
    plt.plot(np.log10(scores[:, :max_step].mean(axis=0)), linestyle="-", linewidth=0.1)
    plt.xlabel("Rounds of betting")
    plt.ylabel("$<log_{10}>$ wealth")
    plt.legend(["Winners", "Losers", "Total"])
    plt.savefig("./plots/hist_means.pdf")

    plt.clf()
    plt.plot(np.log10(hist.T[1]/np.sum(hist[0])), linestyle="--", linewidth=linewidth)
    plt.plot(np.log10(hist.T[0]/np.sum(hist[0])), linestyle=":", linewidth=linewidth)
    plt.xlabel("Rounds of betting")
    plt.ylabel("$log_{10}$ percentage in each group")
    plt.legend(["Winners", "Losers"])
    plt.savefig("./plots/hist.pdf")
    # exit()
    #
    # scores = None
    # plt.clf()
    # scores = np.load("scores_add.npy")
    # print(scores.shape)
    # #exit()
    # # for i in range(20000):
    # #     plt.plot(scores[i][:100], "r+")
    # #mean = scores[:,:10000].mean(axis=0)
    # #exit()
    # mean = (scores > 10)[:, :10000].mean(axis=0)
    # print(mean)
    # plt.plot((mean))
    # plt.savefig("./scores_add.png")

@jit(nopython=True, parallel = True)
def get_histograms(scores, max_step, bins):
    hist = np.zeros(shape = (max_step, len(bins)-1),dtype=np.float64)
    hist_means = np.zeros(shape=(max_step, len(bins) - 1), dtype=np.float64)

    for i in prange(0,max_step):
        hist_data = scores[:, i]
        hist[i] = np.histogram(hist_data, bins = bins)[0]
        bin_indices = np.digitize(hist_data,  bins = bins)
        means  = [hist_data[bin_indices == j].mean() for j in set(bin_indices)]
        if(len(means) == 1):
            hist_means[i] = np.array([means[0], 0.0])
        else:
            hist_means[i] = means
        #print(i,means)

    return hist, hist_means


if __name__ == "__main__":
    main()