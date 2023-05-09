from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas # import FigureCanvas
from matplotlib.figure import Figure # import Figure Artist
import numpy as np

fig = Figure()
canvas = FigureCanvas(fig)

#create 10000 randoms numbers using numpy
x = np.random.randn(10000)

ax = fig.add_subplot(111) #create an axes artists

ax.hist(x,100) #generate a histograme of the 10000 numbers

#add a title to the figure and save it
ax.set_title("Normal distribution with $\mu=0, \sigma=1$")
fig.savefig('matplotlib_histogram.png')

