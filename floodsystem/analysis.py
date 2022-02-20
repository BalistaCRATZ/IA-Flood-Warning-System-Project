import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from datetime import datetime, timedelta

#Function to find the coefficients of the best-fit polynomial f(x)
def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)

    #shifting of the date axis
    p_coeff =np.polyfit(x-x[0], levels, p)

    poly = np.poly1d(p_coeff)

    x1 = np.linspace(x[0], x[-1], 100)
    plt.plot(x1, poly(x1-x[0]), label = "Least-Square Fit")

