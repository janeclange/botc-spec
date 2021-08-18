import pyro.distributions as dist
import math
import numpy as np

tb_townsfolk = ["washerwoman",
                "librarian",
                "investigator",
                "chef",
                "empath",
                "fortune teller",
                "undertaker",
                "monk",
                "ravenkeeper",
                "virgin",
                "slayer",
                "soldier",
                "mayor"]

tb_outsider = ["butler",
               "drunk",
               "recluse",
               "saint"]

tb_minion = ["poisoner",
             "spy",
             "scarlet woman",
             "baron"]

tb_demon = ["imp"]

def roletypes(n): 
    arr = [0,0,0,1]
    if n == 5: 
        arr = [3,0,1,1]
    elif n == 6:
        arr = [3,1,1,1]
    else: 
        arr[1] = (n - 1) % 3 
        arr[2] = (n - 4) // 3
        arr[0] = n - arr[1] - arr[2] - arr[3]
    return arr

def binom(n, k):
    return int(math.factorial(n) / (math.factorial(k) * math.factorial(n-k)))

def uniform(n): 
    #a uniform random element from the set of legal setups for n players
    #this is just for demonstration, you probably shouldn't actually use it --
    #the probability of a baron is often very high or very low depending on n 

    types = roletypes(n)
    num_baron_setups = binom(len(tb_minion), (types[2] - 1)) * binom(len(tb_outsider), (types[1] + 2)) * binom(len(tb_townsfolk), (types[0] - 2))

    num_other_setups = binom(len(tb_minion), (types[2])) * binom(len(tb_outsider), types[1]) * binom(len(tb_townsfolk), types[0])

    has_baron = dist.Bernoulli(num_baron_setups / (num_baron_setups + num_other_setups)).sample().item()

    if has_baron: 
        types[0] = types[0] - 2
        types[1] = types[1] + 2
        minions = np.append(np.random.choice(tb_minion[:-1], types[2] - 1, replace=False), "baron")
    else:
        minions = np.random.choice(tb_minion[:-1], types[2], replace=False)

    townsfolk = np.random.choice(tb_townsfolk, types[0], replace=False)
    outsiders = np.random.choice(tb_outsider, types[1], replace=False)
    demons = np.random.choice(tb_demon, types[3], replace=False) #unnecessary, but whatever
    return [townsfolk, outsiders, minions, demons]

def uniform_minions(n):
    #maybe actually worth using. minions are uniform, then the rest of the setup is 
    #uniform conditioned on the minions.

    types = roletypes(n)
    has_baron = dist.Bernoulli(binom(len(tb_minion), types[2] - 1) / binom(len(tb_minion), types[2])).sample().item()
    
    print(binom(len(tb_minion), types[2] - 1) / binom(len(tb_minion), types[2]))
    if has_baron: 
        types[0] = types[0] - 2
        types[1] = types[1] + 2
        minions = np.append(np.random.choice(tb_minion[:-1], types[2] - 1, replace=False), "baron")
    else:
        minions = np.random.choice(tb_minion[:-1], types[2], replace=False)

    townsfolk = np.random.choice(tb_townsfolk, types[0], replace=False)
    outsiders = np.random.choice(tb_outsider, types[1], replace=False)
    demons = np.random.choice(tb_demon, types[3], replace=False) #unnecessary, but whatever
    return [townsfolk, outsiders, minions, demons]

