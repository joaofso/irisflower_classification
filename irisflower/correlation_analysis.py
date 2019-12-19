from irisflower import data_reader as reader
import matplotlib.pyplot as plt
import numpy as np


def pairwise_correlations(data, graphical=False):
    """
    @param graphical: boolean value indicating the kind of correlation to perform
    @type data: pandas.DataFrame
    """
    corr = data.corr()
    if graphical:
        return graphical_correlation(data, corr)
    else:
        return str(corr)


def graphical_correlation(data, correlation):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(correlation, cmap='coolwarm', vmin=-1, vmax=1)
    fig.colorbar(cax)
    ticks = np.arange(0, len(data.columns), 1)
    ax.set_xticks(ticks)
    plt.xticks(rotation=90)
    ax.set_yticks(ticks)
    ax.set_xticklabels(data.columns)
    ax.set_yticklabels(data.columns)
    return plt
