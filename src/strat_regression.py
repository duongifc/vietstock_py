# If the price is sideway, we expect the slope to be close to 0, or the angle
# of the slope small, say < 10 degree

from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

def slope(df):
    x = np.arange(0, len(df))
    x.resize(len(df),1)
    lr = LinearRegression()
    lr.fit(x, df)
    return(lr)

# angle in degree of slope
def angle_slope(lr):
    slope_in_degree = np.arctan(lr.coef_[0])*180/np.pi
    return(slope_in_degree)

def plot_regression_line(x, y, lr):
    fig, ax = plt.subplots()
    ax.scatter(x, y, color = "red")
    ax.plot(x, lr.predict(x), color = "blue", \
            label = "y = %0.2f x + %0.2f" %(lr.coef_, lr.intercept_) )
    legend = ax.legend(loc='upper right', shadow=True, fontsize='x-large')
    legend.get_frame().set_facecolor('#00FFCC')
    plt.show()
