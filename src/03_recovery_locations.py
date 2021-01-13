import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

file_cxt = '../data/{}_cdf_agg{}.csv' # .format(model,agg)
models=['MADE1','MimSca','FO', 'TDRW', 'BI', 'BF', 'Reactors']
models_comp = ["Reactors","BI", "BF", "TDRW", "MimSca","FO"]
plt.close("all")
plt.rc('text', usetex=True)

agg = 10         # no data aggregation, fine scale resolution
it = 2     # time step i = 2 --> 126d
cr= [0.05, 0.5, 0.95]

### MADE data
data = np.loadtxt(file_cxt.format('MADE1', agg), delimiter=";")
xr_MADE = np.interp(cr, data[1:,it], data[1:,0]) 

absolute_rates=np.zeros((len(cr),len(models_comp)))
relative_rates=np.zeros((len(cr),len(models_comp)))

for im, model in enumerate(models_comp):

    ### calculate recovery mass locations specified by rates
    data = np.loadtxt(file_cxt.format(model, agg), delimiter=";")
    xr =  np.interp(cr, data[1:,it], data[1:,0]) 

    absolute_rates[:,im]=(xr-xr_MADE)
    relative_rates[:,im]=(xr-xr_MADE)/xr_MADE

fig = plt.figure(figsize= [5,3.5] ) 

for ir, rr in enumerate(cr):
    ax1 = fig.add_subplot(1, len(cr), ir + 1)
    ax1.barh(range(len(models_comp)), relative_rates[ir,:],color = mcolors.TABLEAU_COLORS) #colors)


    ### Modify positions of axis
    xlim = max(abs(relative_rates[ir,:]))
    ax1.set_xlim([-xlim, xlim])

    # Move left y-axis and bottom x-axis to centre, passing through (0,0)
    ax1.spines["left"].set_position("center")
    # Eliminate upper and right axes
    ax1.spines["right"].set_color("none")
    ax1.spines["top"].set_color("none")
    ax1.set_xlabel(r"\textup{{MADE}} $x_{{{}\%}}$ [m]".format(int(100 * rr)))
    ax1.set_xticks([0])
    ax1.set_xticklabels([round(xr_MADE[ir], ndigits=1)])
    ax1.set_yticks([])
    for im,model in enumerate(models_comp):
        if ir == 0:
            plt.text(-4.8, im, "{}".format(model))
        plt.text(0.15 * xlim,im + 0.15,"${:.1f}$ m".format(absolute_rates[ir,im]))           
        plt.text(0.15 * xlim,im - 0.25,"$({:.0f}\%)$".format(100 * relative_rates[ir,im]))



