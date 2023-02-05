import numpy as np
from matplotlib import pyplot as plt


def cdf_plot(matrix):

    plt.rcParams["figure.autolayout"] = True
    plt.rcParams["figure.figsize"] = [10, 5]
    # get values in the matrix as a simple list
    values = matrix.tolist()[0]
    # histogram values
    count, bins_count = np.histogram(values, bins=10)
    # probability density function from histogram
    pdf = count / sum(count)
    # cumulative distribution function from pdf
    cdf = np.cumsum(pdf)
    # Plot cdf and show
    plt.plot(bins_count[1:], cdf, label="CDF")
    plt.legend()
    plt.show()
