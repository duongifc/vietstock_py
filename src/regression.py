from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

def slope(df):
    x = np.arange(0, len(df))
    x.resize(len(df),1)
    lr = LinearRegression()
    lr.fit(x, df)
    return(lr)

def plot_regression_line(x, y, lr):
    fig, ax = plt.subplots()
    ax.scatter(x, y, color = "red")
    ax.plot(x, lr.predict(x), color = "blue", \
            label = "y = %0.2f x + %0.2f" %(lr.coef_, lr.intercept_) )
    legend = ax.legend(loc='upper right', shadow=True, fontsize='x-large')
    legend.get_frame().set_facecolor('#00FFCC')
    plt.show()
