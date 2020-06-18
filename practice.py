import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

seq1 = [np.random.randint(-1, 2) for _ in range(100)]
seq2 = [np.random.randint(-1, 2) for _ in range(100)]

x = np.arange(100)
y1 = np.cumsum(seq1)
y2 = np.cumsum(seq2)

ax.plot(x, y1, color='blue')
ax.plot(x, y2, color='red')

cross_points = []
idx = 0
while idx < len(x)-1:
    x3 = np.linspace(x[idx], x[idx+1])
    y1_new = np.linspace(y1[idx], y1[idx+1])
    y2_new = np.linspace(y2[idx], y2[idx+1])

    tmp_idx = np.argwhere(np.isclose(y1_new, y2_new, atol=0.1)).reshape(-1)
    if tmp_idx.size != 0:
        cross_point_coords = {'x': x3[tmp_idx], 'y': y2_new[tmp_idx]}
        cross_points.append(cross_point_coords)
        ax.plot(x3[tmp_idx], y2_new[tmp_idx], 'go')

    idx += 1
    
print(cross_points)
plt.show()
