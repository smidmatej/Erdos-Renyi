from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import seaborn as sns

import networkx as nx


animation.writer = animation.writers['ffmpeg']
   
plt.style.use('fast')
#sns.set_style("whitegrid")
interval = 100 # ms
number_of_frames = 100
fps = 1000/interval
print('Creating animation...')
print(f'Number of frames: {number_of_frames}, fps: {fps}, duration: {number_of_frames*interval/1000} s')

n_V = 30

G_ws = nx.watts_strogatz_graph(n_V, 6, 0.5)
pos0 = nx.shell_layout(G_ws)
xy0 = np.array([pos0[i] for i in range(n_V)]).T

pbar = tqdm(total=number_of_frames)

fig = plt.figure(figsize=(10,10), dpi=100)

xmin = np.min(xy0[0])
xmax = np.max(xy0[0])
ymin = np.min(xy0[1])
ymax = np.max(xy0[1])


xymin = np.min([xmin, ymin])
xymax = np.max([xmax, ymax])*1.1
if xymin < 0:
    xymin = xymin*2
else:
    xymin = xymin*0.5

if xymax < 0:
    xymax = xymax*0.5
else:
    xymax = xymax*2



def animate(i):
    fig.clear()
    ax = plt.gca()
    ax.set_xlim([xymin, xymax])
    ax.set_ylim([xymin, xymax])
    #breakpoint()
    phi = i/number_of_frames*2*np.pi
    R = np.array([[np.cos(phi), -np.sin(phi)], [np.sin(phi), np.cos(phi)]])

    xy = R @ xy0
    #breakpoint()
    posdict = {i: (xy[0][i], xy[1][i]) for i in range(n_V)}
    nx.draw_networkx(G_ws, pos=posdict, with_labels=False, style='-', node_size=100, node_color='grey', alpha=0.8, width=0.5, edge_color='k')

    pbar.update()
        
ani = animation.FuncAnimation(fig, animate, frames=number_of_frames, interval=interval)       

ani.save('rotate_g' + '.gif', writer='imagemagick', fps=fps, dpi=100)
#plt.show()