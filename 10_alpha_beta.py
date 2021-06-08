import numpy as np

import utils
import pandas as pd
import matplotlib.pyplot as plt


if __name__ == "__main__":
    symbols = ['SPY', 'XOM', 'GLD']
    dates = pd.date_range('2020-03-01', '2021-05-31')
    df: pd.DataFrame = utils.get_data(symbols, dates)

    daily_ret = utils.compute_daily_returns(df)

    daily_ret.plot(kind='scatter', x='SPY', y='XOM')
    beta_XOM, alpha_XOM = np.polyfit(daily_ret['SPY'], daily_ret['XOM'], 1)
    plt.plot(daily_ret['SPY'], beta_XOM * daily_ret['SPY'] + alpha_XOM, '-', color='r')
    plt.show()

    daily_ret.plot(kind='scatter', x='SPY', y='GLD')
    beta_GLD, alpha_GLD = np.polyfit(daily_ret['SPY'], daily_ret['GLD'], 1)
    plt.plot(daily_ret['SPY'], beta_GLD * daily_ret['SPY'] + alpha_GLD, '-', color='r')
    plt.show()

    print(daily_ret.corr(method='pearson'))