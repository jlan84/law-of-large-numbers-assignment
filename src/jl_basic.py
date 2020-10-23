import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import time

plt.style.use('fivethirtyeight')
font = {'weight': 'bold', 'size': 16}
plt.rc('font', **font)

def flip_coin(n_flips, p=0.5):
    flips = stats.binom(n=1, p=p).rvs(n_flips)
    return flips

def plot_averages(ax, x, y, expected_val, label=None):
    ax.plot(x, y, label=label, linewidth=1)
    ax.axhline(expected_val, linestyle='--', color='black', linewidth=1)
    # ax.set_ylim(0,1)

def mult_exp(beg, end , step, p=0.5):
    samples = np.arange(beg, end, step=step)
    output = [np.mean(flip_coin(n,p=p)) for n in samples]
    return output

def mult_means(n_flips=100, repeat=100, p=0.5):
    means = [np.mean(flip_coin(n_flips=n_flips,p=p)) for i in range(repeat)]
    return np.var(means)
    

if __name__ == "__main__":
    """ 
    #2 Sample average should be 0.5 due to the law of large numbers, the average
    converges towards the expected value.
    """
    print(np.mean(flip_coin(1000)))

    #3 Sample average converges towards the probability

    print(np.mean(flip_coin(1000,p=0.2)))

    #4
    start = time.time()
    sample_sizes = np.arange(10, 1001, step=10)
    averages = [np.mean(flip_coin(n_flips=n)) for n in sample_sizes]
    averages = list(map(np.mean,list(map(flip_coin, sample_sizes))))
    fig, ax = plt.subplots(figsize=(12,2))
    plot_averages(ax, sample_sizes, averages, 0.5)

    experiments = 100
    many_averages = []
    for i in range(experiments):
        many_averages.append(mult_exp(10,1001,10))
    
    fig, ax = plt.subplots(figsize=(10,1))
    for val in many_averages:
        plot_averages(ax,sample_sizes,val,0.5)
    plt.tight_layout()
    
    probs = [0.1,0.25,0.5,0.75,0.9]
    titles = ['prob = 0.1', 'prob = 0.25', 'prob = 0.5', 'prob = 0.75',
              'prob = 0.9']
    
    fig, axs = plt.subplots(5,1, figsize=(10,8))

    for prob, title, ax in zip(probs, titles, axs.flatten()):
        experiments = 50
        lst = [mult_exp(10,1001,10,p=prob) for i in range(experiments)]
        for val in lst:
            plot_averages(ax, sample_sizes,val,prob)
        ax.set_title(title)
    plt.tight_layout()
    
    probs = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

    variances = [mult_means(p=p) for p in probs]
    
    fig, ax = plt.subplots()
    ax.plot(probs, variances)
    plt.show()
    
    print(f'This took {time.time()-start} seconds')
    
    
    

    
    
    