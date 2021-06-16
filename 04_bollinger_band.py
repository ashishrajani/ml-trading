import utils
import pandas as pd
import matplotlib.pyplot as plt


if __name__ == "__main__":
    symbols = ['SPY']
    window_size = 20
    dates = pd.date_range('2020-03-01', '2021-05-31')
    df: pd.DataFrame = utils.get_data(symbols, dates)

    ax = df['SPY'].plot(title='SPY rolling mean', color="black")

    rm_SPY = utils.get_rolling_mean(df, window_size)
    rstd_SPY = utils.get_rolling_std(df, window_size)
    upped_band, lower_band = utils.get_bollinger_band(rm_SPY, rstd_SPY)

    rm_SPY.plot(ax=ax, color="red")
    upped_band.plot(ax=ax, color="orange")
    lower_band.plot(ax=ax, color="orange")

    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend(["SPY", "Rolling Mean", "Upper Bound", "Lower Bound"], loc='upper left')
    plt.show()