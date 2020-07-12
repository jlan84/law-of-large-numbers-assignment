import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


def flip_coin(n_flips, p=0.5):
    flips = stats.binom(n=1, p=p).rvs(n_flips)
    return flips

flips = flip_coin(1000)    
print(np.mean((flips)))

flips = flip_coin(1000, p=0.7)  
print(np.mean(flips))  


list_of_ten = list(range(10,1001,10))


flip_avg = []
for val in list_of_ten:
    flip_avg.append(np.mean(flip_coin(val)))

# fig, ax = plt.subplots(1, 1, figsize=(5,5))

# ax.plot(list_of_ten, flip_avg)
# ax.axhline(0.5, color='grey')
# plt.show()

def make_sample_mean_path(begin, end, step, p=0.5):
    flp_lst = list(range(begin, end, step))
    flp_avg = []
    for val in flp_lst:
        flp_avg.append(np.mean(flip_coin(val,p=p)))
    return flp_lst, flp_avg
flp_lst, flp_avg = make_sample_mean_path(10,1001,10)


probs = [.1,.25,.5,.75,.9]

# fig, axs = plt.subplots(nrows=5, ncols=1, figsize=(12,10))

# for prob, ax in zip(probs, axs.flatten()):
#     for j in range(100):
#         flp_lst, flp_avg = make_sample_mean_path(10,1001,10,p=prob)
#         ax.plot(flp_lst, flp_avg)
#     ax.axhline(y=prob, color='grey', linestyle='--')
#     ax.set_ylim(-.25,1.25)

# plt.show()

fairness = [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
flips_list = []
for prob in fairness:
    flip_mean = []
    for j in range(100):
        flip_mean.append(np.mean(flip_coin(100,p=prob)))
    flips_list.append(np.var(flip_mean))

fix, ax = plt.subplots(figsize=(12,6))

ax.scatter(fairness, flips_list)
ax.set_xlabel('fairness')
ax.set_ylabel('variance')
plt.show()


# def sample_poisson(sample_size, lam=1.0):
#     return stats.poisson(mu=lam).rvs(sample_size)

# print(np.mean(sample_poisson(1000)))
# print(np.mean(sample_poisson(1000,lam=2)))
# range_lst = list(range(10,1001,10))
# poission_dist = []
# for val in range_lst:
#     poission_dist.append(np.mean(sample_poisson(val)))

# fig, ax = plt.subplots(figsize=(12,4))

# ax.plot(range_lst, poission_dist)
# plt.show()

# def sample_mean_path(beg, end, step, lam=1.0):
#     sample_size = list(range(beg, end, step))
#     poission_dist = []
#     for val in sample_size:
#         poission_dist.append(np.mean(sample_poisson(val,lam=lam)))
#     return sample_size, poission_dist

# fig, ax = plt.subplots(1,1, figsize=(12,4))
# ax.axhline(1.0, color='grey', linestyle='--')

# for i in range(100):
#     x, y = sample_mean_path(10,1001,10)
#     ax.plot(x,y)

# ax.set_ylim(-.25,2)
# plt.show()


# lamdas = [1,2,3,4,5]
# fig, axs = plt.subplots(5,1, figsize=(15,6))


# for i in range(len(lamdas)):
#     for j in range(100):
#         x,y = sample_mean_path(10,1001,10,lam=lamdas[i])
#         axs[i].plot(x,y)
#     axs[i].axhline(y=lamdas[i], c='grey', linestyle='--')
#     axs[i].set_ylim(-.25,2)

# plt.tight_layout()
# plt.show()

# fairness = [1,2,3,4,5,6,7,8,9,10]
# variance = []
# for lm in fairness:
#     lam_mean = []
#     for i in range(100):
#         lam_mean.append(np.mean(sample_poisson(100,lam=lm)))
#     variance.append(np.var(lam_mean))

# print(variance)

# fig, ax = plt.subplots(figsize=(12,5))

# ax.plot(fairness, variance)
# plt.show()


# plt.style.use('ggplot')
# lunch = stats.norm(loc=2, scale=0.5)
# x = np.linspace(0.5, 3.5, num=100)
# print(lunch.ppf(.998))
# fig, ax = plt.subplots(figsize=(6,4))
# ax.plot(x, lunch.pdf(x), c='black', label='distribution')
# ax.set_title('Google lunch distribution')
# ax.set_ylabel('pdf')
# ax.set_xlabel('time taken for lunch')

# ax.axvline(lunch.ppf(.025), c="red",linestyle="--", linewidth=1)
# ax.axvline(lunch.ppf(.975),c="red", linestyle="--", linewidth=1)
# x1 = lunch.ppf(.025)
# x2 = lunch.ppf(.975)
# x = np.linspace(x1, x2, num=100)
# ax.fill_between(x=x, y1=lunch.pdf(x), alpha=.2, label='Middle 95%')
# ax.legend()
# plt.show()

# binomial = stats.binom(10000, 0.5).rvs(10000)
# mean = np.mean(binomial)
# std = np.std(binomial)
# print(mean)
# print(std)
# normal = stats.norm(loc=mean, scale=std).rvs(10000)
# norm_mean = np.mean(normal)
# norm_std = np.mean(normal)
# print(norm_mean)
# print(norm_std)