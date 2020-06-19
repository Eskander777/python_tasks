import matplotlib.pyplot as plt
import numpy as np


def make_cumsum():
    '''Creates sequence'''
    seq1 = [np.random.randint(-1, 2) for _ in range(100)]
    seq2 = np.cumsum(seq1)
    return seq2


def visualize(y1, y2):
    '''Visualizes graphs and shows intersections.'''
    x = np.arange(len(y1))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y1, color='blue')
    ax.plot(x, y2, color='red')

    cross_points = []
    idx = 0
    while idx < len(x)-1:
        x3 = np.linspace(x[idx], x[idx+1])
        y1_new = np.linspace(y1[idx], y1[idx+1])
        y2_new = np.linspace(y2[idx], y2[idx+1])
        tmp_idx = np.argwhere(np.isclose(y1_new, y2_new, atol=0.001)).reshape(-1)

        if tmp_idx.size != 0:
            cross_point_coords = {'x': x3[tmp_idx], 'y': y2_new[tmp_idx]}
            cross_points.append(cross_point_coords)
            ax.plot(x3[tmp_idx], y2_new[tmp_idx], 'go')

        idx += 1

    print(cross_points)
    plt.show()


def main():
    seq1 = make_cumsum()
    seq2 = make_cumsum()
    visualize(seq1, seq2)


if __name__ == '__main__':
    main()
