from matplotlib import pyplot as plt
import numpy as np
from plot import get_histograms

plt.style.use('seaborn')


def main():
    scores = np.load("scores_mult.npy")

    bins = np.array([0.0, 10.0, np.inf])
    max_step = 300

    linewidth = 1.5

    hist, hist_means = get_histograms(scores, max_step, bins)

    plt.plot((hist_means.T[1]), linestyle = "-", linewidth=linewidth)
    plt.plot((hist_means.T[0]), linestyle = "-", linewidth=linewidth)
    plt.plot((scores[:, :max_step].mean(axis=0)), linestyle="-", linewidth=0.1)
    plt.xlabel("Rounds of betting")
    plt.ylabel("Wealth")
    plt.legend(["Winners", "Losers", "Total"])
    plt.savefig("./plots/hist_means_less_rounds.pdf")

    plt.clf()
    plt.plot((hist.T[1]/np.sum(hist[0])), linestyle="-", linewidth=linewidth)
    plt.plot((hist.T[0]/np.sum(hist[0])), linestyle="-", linewidth=linewidth)
    plt.xlabel("Rounds of betting")
    plt.ylabel("Percentage in each group")
    plt.legend(["Winners", "Losers"])
    plt.savefig("./plots/hist_less_rounds.pdf")
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




if __name__ == "__main__":
    main()