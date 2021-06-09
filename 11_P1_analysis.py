import utils
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    symbols = ['AAPL', 'XOM', 'IBM', 'PG']
    start_date = '2020-03-01'
    end_date = '2021-05-31'
    dates = pd.date_range(start_date, end_date)
    allocations = [0.3, 0.2, 0.4, 0.1]
    start_inv = 100000
    risk_free_rate = 0.0
    sampling_freq = 252

    df: pd.DataFrame = utils.get_data(symbols, dates)
    utils.plot_selected(df, symbols, start_date, end_date)

    prices_stock = df[symbols]
    price_SPY = df['SPY']

    normed_prices = prices_stock / prices_stock.values[0]
    allocated = normed_prices.multiply(allocations)
    position_value = allocated.multiply(start_inv)
    portfolio_value = position_value.sum(axis=1)

    daily_return = utils.compute_daily_returns(portfolio_value)
    cumulative_return = utils.compute_cumulative_returns(portfolio_value)

    sharpe_ratio = utils.compute_sharpe_ratio(sampling_freq, risk_free_rate, daily_return)

    print('Sharpe Ratio: ', sharpe_ratio)

    port_val = portfolio_value / portfolio_value[0]
    prices_SPY = price_SPY / price_SPY[0]
    df_temp = pd.concat([port_val, prices_SPY], keys=['Portfolio', 'SPY'], axis=1)
    utils.plot_data(df_temp, title="Daily portfolio value and SPY")