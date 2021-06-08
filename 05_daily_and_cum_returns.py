import utils
import pandas as pd


def compute_daily_returns(df: pd.DataFrame) -> pd.DataFrame:
    daily_returns = df.copy()
    # daily_returns[1:] = (daily_returns[1:] / daily_returns[:-1].values) - 1
    daily_returns = daily_returns / daily_returns.shift(1) -1
    daily_returns.iloc[0, :] = 0
    return daily_returns


def compute_cumulative_returns(df: pd.DataFrame) -> pd.DataFrame:
    cum_returns = df.copy()
    cum_returns = cum_returns / cum_returns.iloc[0] - 1
    cum_returns.iloc[0, :] = 0
    return cum_returns


if __name__ == "__main__":
    symbols = ['SPY', 'XOM']
    dates = pd.date_range('2020-03-01', '2021-05-31')
    df: pd.DataFrame = utils.get_data(symbols, dates)
    utils.plot_data(df)

    daily_returns = compute_daily_returns(df)
    utils.plot_data(daily_returns, "Daily Returns")

    cumm_returns = compute_cumulative_returns(df)
    utils.plot_data(cumm_returns, "Cumulative Returns")

