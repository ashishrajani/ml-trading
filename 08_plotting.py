import utils
import pandas as pd
import matplotlib.pyplot as plt


if __name__ == "__main__":
    symbols = ['SPY']
    dates = pd.date_range('2020-03-01', '2021-05-31')
    df: pd.DataFrame = utils.get_data(symbols, dates)
    utils.plot_data(df)

    daily_ret = utils.compute_daily_returns(df)
    utils.plot_data(daily_ret, "Daily Returns")

    daily_ret.hist(bins=20)

    mean = daily_ret['SPY'].mean()
    std = daily_ret['SPY'].std()
    print('Mean', mean)
    print('Std. Dev.', std)

    plt.axvline(mean, color='w', linestyle='dashed', linewidth=2)
    plt.axvline(-std, color='r', linestyle='dashed', linewidth=2)
    plt.axvline(std, color='r', linestyle='dashed', linewidth=2)
    plt.show()

    kurtosis = daily_ret['SPY'].kurtosis()
    print('Kustosis ', kurtosis)

    symbols = ['SPY']
    dates = pd.date_range('2020-03-01', '2021-05-31')
    df: pd.DataFrame = utils.get_data(symbols, dates)
    utils.plot_data(df)