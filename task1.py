import matplotlib.pyplot as plt
import numpy as np


def make_cumsum():
    seq1 = [np.random.randint(-1, 2) for _ in range(100)]
    seq2 = np.cumsum(seq1)
    return seq2


def visualize(seq1, seq2):
    same_values = np.intersect1d(seq1, seq2)
    raw_idx = np.argwhere(np.isclose(seq1, seq1, atol=0.1)).reshape(-1)
    x = np.arange(100)
    idx = [index for index in raw_idx if seq1[index] == seq2[index]]
    inter_points_coords = [{'x': index, 'y': seq1[index]} for index in idx]
    print(inter_points_coords)
    plt.plot(x, seq1, color="blue")
    plt.plot(x, seq2, color="red")
    plt.plot(x[idx], seq1[idx],  'go')
    plt.show()


seq1 = make_cumsum()
seq2 = make_cumsum()
visualize(seq1, seq2)
