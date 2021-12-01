import pandas as pd
import numpy as np


def count_increases(dist_vec):
    delta_vec = dist_vec[1:] - dist_vec[:-1]
    return int(sum(delta_vec > 0))

def window_sum(vec, n=3):
    m = len(vec)
    assert(m >= n)
    sum_vec = np.array([sum(vec[i:i+n]) for i in range(m)])
    return sum_vec


def main():
    df = pd.read_csv("day1input.csv",header=None)
    num_increases = count_increases(df.values)
    print("There are {:,} depth increases.".format(num_increases))

    windowed_vec = window_sum(df.values)
    num_increases = count_increases(windowed_vec)
    print("There are {:,} depth increases in the moving average.".format(num_increases))

if __name__ == '__main__':
    main()
