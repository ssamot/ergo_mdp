from scipy.stats import lognorm
import numpy as np
from matplotlib import pyplot as plt
plt.style.use('seaborn')

stddev = 14
mean = 12
dist=lognorm([stddev],loc=mean)

x=np.linspace(mean,200,200)
plt.plot(x,dist.pdf(x))
#plt.plot(x,dist.cdf(x))
plt.savefig("./lognorm.pdf")