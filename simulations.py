import numpy as np
from numba import jit, njit, prange

def main():

    num_simulations = 400000
    rounds = 3000
    starting_capital = 10
    np.random.seed(0)

    final_scores = simulation_mul(num_simulations, starting_capital, rounds)
    np.save("./scores_mult.npy", final_scores)
    final_scores = None
    final_scores = simulation_add(num_simulations, starting_capital, rounds)
    np.save("./scores_add.npy", final_scores)



@njit(parallel=True)
def simulation_mul(num_simulations, starting_capital, rounds):
    final_scores = np.zeros(shape=(num_simulations, rounds))
    for i in prange(num_simulations):
        final_capital = single_run_mul(starting_capital, rounds)
        final_scores[i] = final_capital
    return final_scores


@njit(parallel=True)
def simulation_add(num_simulations, starting_capital, rounds):
    final_scores = np.zeros(shape=(num_simulations, rounds))
    for i in prange(num_simulations):
        final_capital = single_run_add(starting_capital, rounds)
        final_scores[i] = final_capital
    print(final_scores.shape)
    return final_scores


@jit(nopython=True)
def single_run_mul(starting_capital, rounds):
    current_capital = starting_capital
    steps = np.zeros(shape=rounds)
    for i in range(rounds):
        if(np.random.random() < 0.5):
            current_capital = growth_mult(current_capital, -0.4)
        else:
            current_capital = growth_mult(current_capital, 0.5)
        steps[i] = current_capital

    return steps

@jit(nopython=True)
def single_run_add(starting_capital, rounds):
    current_capital = starting_capital
    steps = np.zeros(shape=rounds)
    for i in range(rounds):
        if(np.random.random() < 0.5):
            current_capital = growth_add(current_capital, -4.0)
        else:
            current_capital = growth_add(current_capital, 5.0)
        #print(current_capital, "current")
        steps[i] = current_capital

    return steps

@jit(nopython=True)
def growth_mult(capital, perc):
    capital+=capital*perc
    return capital

@jit(nopython=True)
def growth_add(capital, value):
    #print(capital,value)
    capital+=value
    return capital

if __name__ == "__main__":
    main()

