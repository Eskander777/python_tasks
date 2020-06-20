import matplotlib.pyplot as plt
import numpy as np


class NumberArray():
    """Number array to put on graph"""

    def __init__(self):
        self.seq1 = [np.random.randint(-1, 2) for _ in range(100)]
        self.seq2 = np.cumsum(self.seq1)
        self.length = len(self.seq2)


def visualize(y1, y2):
    """Visualizes graphs and shows intersections"""
    x = np.arange(y1.length)
    y1 = y1.seq2
    y2 = y2.seq2
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y1, color='blue')
    ax.plot(x, y2, color='red')

    cross_points = []
    for idx in x[:-1]:
        x3 = np.linspace(x[idx], x[idx+1], num=1000)
        y1_new = np.linspace(y1[idx], y1[idx+1], num=1000)
        y2_new = np.linspace(y2[idx], y2[idx+1], num=1000)
        tmp_idx = np.argwhere(np.isclose(
            y1_new, y2_new, atol=0.001)).reshape(-1)

        if tmp_idx.size != 0:
            cross_point_coords = {'x': x3[tmp_idx], 'y': y2_new[tmp_idx]}
            cross_points.append(cross_point_coords)
            ax.plot(x3[tmp_idx], y2_new[tmp_idx], 'go')

    print(cross_points)
    plt.show()


def main():
    array_to_graph1 = NumberArray()
    array_to_graph2 = NumberArray()
    visualize(array_to_graph1, array_to_graph2)


if __name__ == '__main__':
    main()
