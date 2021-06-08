import utils
import pandas as pd
import matplotlib.pyplot as plt


if __name__ == "__main__":
    symbols = ['SPY', 'XOM']
    dates = pd.date_range('2020-03-01', '2021-05-31')
    df: pd.DataFrame = utils.get_data(symbols, dates)

    daily_ret = utils.compute_daily_returns(df)

    daily_ret['SPY'].hist(bins=20, label='SPY')
    daily_ret['XOM'].hist(bins=20, label='XOM')

    plt.legend(["SPY", "XOM"], loc='upper left')
    plt.show()