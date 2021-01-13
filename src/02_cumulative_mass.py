import numpy as np
import matplotlib.pyplot as plt

### aggregation level
# agg = 10      # dx = 10m (uscaled, aggregated data)
agg = 10         # no data aggregation, fine scale resolution
it = 2     # time step i = 2 --> 126d

file_cxt = '../data/{}_cdf_agg{}.csv' # .format(model,agg)
models=['MADE1','MimSca','FO', 'TDRW', 'BI', 'BF', 'Reactors']
plt.close("all")
plt.rc('text', usetex=True)

fig = plt.figure(figsize=[4.5,3.5])
ax = fig.add_subplot(1, 1, 1)

for im, model in enumerate(models):    
    data = np.loadtxt(file_cxt.format(model, agg), delimiter=";")
    x = data[1:,0]
    cxt = data[1:,it]
    ### determine mass recovery locations
    cr= [0.05, 0.5, 0.95]
    xr = np.interp(cr, cxt, x)

    if not (model == 'MADE1' and (agg == 0 or it ==7)):
        ax.plot(x,cxt,lw=2, ls="-",c= 'C{}'.format(im),label = model)    
        for ir, rr in enumerate(cr):
             ax.plot([xr[ir], xr[ir]],[0, max(cr[ir], 0.2)], color='C{}'.format(im),ls='--',lw=1.5)

    ax.set_ylabel(r"Cumulative mass")
    ax.set_xlabel(r"Travel distance $x$  [m]")
    ax.set_xlim([-16,70])
    ax.grid(True)
    ax.legend(loc='upper left')#bbox_to_anchor=(0.95, 0.1))  # ,ncol=ncols,numpoints=1)
    ax.text(0.8,0.5, r"$T={}$d".format(int(data[0,it])), bbox=dict(facecolor="w",boxstyle='round'), transform=ax.transAxes)
