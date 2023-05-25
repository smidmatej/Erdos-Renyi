

from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import seaborn as sns

import networkx as nx


animation.writer = animation.writers['ffmpeg']
interval = 20 # 50 fps    
plt.style.use('fast')
#sns.set_style("whitegrid")
number_of_frames = 25
print('Creating animation...')
print(f'Number of frames: {number_of_frames}, fps: {1000/interval}, duration: {number_of_frames*interval/1000} s')

n_V = 30

x = np.linspace(0, 2*np.pi, n_V)


G_ws = nx.watts_strogatz_graph(n_V, 3, 0.7)

pbar = tqdm(total=number_of_frames)

fig = plt.figure(figsize=(10,10), dpi=100)

def animate(i):
    fig.clear()
    #breakpoint()
    y = np.sin(x*(i+number_of_frames)/number_of_frames)
    posdict = {i: (x[i], y[i]) for i in range(n_V)}
    nx.draw_networkx(G_ws, pos=posdict, with_labels=False, style='--', node_size=100, node_color='r', alpha=0.8, width=0.5, edge_color='b')
    
    pbar.update()
        
ani = animation.FuncAnimation(fig, animate, frames=number_of_frames, interval=interval)       

ani.save('sine' + '.gif', writer='imagemagick', fps=10, dpi=100)
#plt.show()