import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import time

plt.style.use('fivethirtyeight')
font = {'weight': 'bold', 'size': 16}
plt.rc('font', **font)

def sample_poisson(n_samples, lam=1):
    return stats.poisson(mu=lam).rvs(n_samples)

def plot_averages(ax, x, y, expected_val, label=None):
    ax.plot(x, y, label=label, linewidth=1)
    ax.axhline(expected_val, linestyle='--', color='black', linewidth=1)
    # ax.set_ylim(0,1)

def mult_exp(beg, end , step, lam=1):
    samples = np.arange(beg, end, step=step)
    output = [np.mean(sample_poisson(n,lam=lam)) for n in samples]
    return output

def mult_means(lam, n_samples=100, repeat=100):
    means = [np.mean(sample_poisson(n_samples=n_samples, lam=lam)) for i in range(repeat)]
    return np.var(means)


if __name__ == "__main__":

    """
    #2 the sample mean for 1000 samples with a lambda of 1 is 1.072
    """
    print(np.mean(sample_poisson(1000)))
    print(np.mean(sample_poisson(1000, lam=0.5)))
    sample_size = np.arange(10,1001,10)
    poisson_range = mult_exp(10,1001,10)
    
    fig, ax = plt.subplots(figsize=(10,2))
    for i in range(100):
        poisson_range = mult_exp(10,1001,10)
        plot_averages(ax, sample_size, poisson_range, 1)
    plt.tight_layout()
    plt.show()
    
    lambdas = [1,2,3,4,5]
    titles = ['lambda = 1', 'lambda = 2', 'lambda = 3', 'lambda = 4',
              'lambda = 5']
    fig, axs = plt.subplots(5,1, figsize=(10,8))

    for lam, title, ax in zip(lambdas, titles, axs.flatten()):
        for i in range(50):
            poisson_range = mult_exp(10,1001,10,lam=lam)
            plot_averages(ax, sample_size, poisson_range, expected_val=lam)
        ax.set_title(title)
    
    plt.tight_layout()
    plt.show()

    lambdas = [0,1,2,3,4,5,8,9,10]
    variances = list(map(mult_means, lambdas))
    fig, ax = plt.subplots()
    ax.plot(lambdas, variances)
    plt.show()
