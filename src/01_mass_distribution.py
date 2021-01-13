import numpy as np
import matplotlib.pyplot as plt

### aggregation level
# agg = 10      # dx = 10m (uscaled, aggregated data)
agg = 0         # no data aggregation, fine scale resolution

### display
yscale = 'log'          # for log scale
# yscale = 'linear'     # for linear scale

### time step choice
it = 2     # time step i = 1 --> 126d

file_cxt = '../data/{}_pdf_agg{}.csv' # .format(model,agg)
models=['MADE1','MimSca','FO', 'TDRW', 'BI', 'BF', 'Reactors']
plt.close("all")
plt.rc('text', usetex=True)

fig = plt.figure(figsize=[4.5,3.5])
ax = fig.add_subplot(1, 1, 1)

for model in models:    
    data = np.loadtxt(file_cxt.format(model, agg), delimiter=";")
    x = data[1:,0]
    cxt = data[1:,it]
    if agg == 0 :
        if model != 'MADE1':
            ax.plot(x,cxt,lw=2, ls="-",label = model)    
        ax.set_ylim([0.0007,0.2])
    else: 
        ax.plot(x,cxt,lw=2, ls="-", marker="o", ms=4.0,label = model)    
        ax.set_ylim([0,0.165])
    ax.set_ylabel(r"Mass distribution $\langle \bar m(x) \rangle$")
    ax.set_xlabel(r"Travel distance $x$  [m]")
    ax.set_xlim([-16,70])
    ax.grid(True)
    ax.legend(loc='upper right')#bbox_to_anchor=(0.95, 0.1))  # ,ncol=ncols,numpoints=1)
    ax.text(0.4,0.85, r"$T={}$d".format(int(data[0,it])), bbox=dict(facecolor="w",boxstyle='round'), transform=ax.transAxes)
    ax.set_yscale(yscale)
