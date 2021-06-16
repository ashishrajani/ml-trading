import utils
import numpy as np
import pandas as pd
from typing import List
import scipy.optimize as spo


def f(allocations: np.array, starting_investment: float, normed_prices):
    allocated = normed_prices.multiply(allocations)
    position_values = allocated.multiply(starting_investment)
    portfolio_value = position_values.sum(axis=1)
    daily_return = (portfolio_value/portfolio_value.shift(1)) - 1
    return utils.compute_sharpe_ratio(252, 0.0, daily_return) * -1


def optimize_portfolio(starting_investment: float, risk_free_rate: float, sampling_frequency: float,
                       symbols: List, allocations: np.array, start_date: str, end_date: str,
                       plot_data = False):
    date_range = pd.date_range(start_date, end_date)

    prices_df: pd.DataFrame = utils.get_data(symbols, date_range)
    prices_df.fillna(method="ffill", inplace=True)
    prices_df.fillna(method="bfill", inplace=True)

    utils.plot_selected(prices_df, symbols, start_date, end_date)

    prices_symbols = prices_df[symbols]
    prices_SPY = prices_df['SPY']

    normed_prices = prices_symbols / prices_symbols.values[0]

    bounds = [(0.0, 1.0) for i in normed_prices.columns]
    constraints = ({'type': 'eq', 'fun': lambda inputs: 1.0 - np.sum(inputs)})

    result = spo.minimize(f, allocations, args=(starting_investment, normed_prices, ), method='SLSQP',
                             constraints=constraints, bounds=bounds, options={'disp': True})

    opt_allocation = result.x
    opt_allocation_std_dr = result.fun
    opt_allocated = normed_prices.multiply(opt_allocation)
    opt_position_value = opt_allocated.multiply(starting_investment)
    opt_port_value = opt_position_value.sum(axis=1)

    daily_return = (opt_port_value/opt_port_value.shift(1)) - 1
    cum_return = (opt_port_value[-1] / opt_port_value[0]) - 1
    avg_daily_return = daily_return.mean()
    std_daily_return = daily_return.std()
    sharpe_ratio = utils.compute_sharpe_ratio(sampling_frequency, risk_free_rate, daily_return)

    if plot_data:
        normed_opt_port_value = opt_port_value / opt_port_value.values[0]
        normed_prices_SPY = prices_SPY / prices_SPY.values[0]
        utils.plot_data(pd.concat([normed_opt_port_value, normed_prices_SPY], keys=['Portfolio', 'SPY'], axis=1), 'Daily Portfolio and SPY values')

    return opt_allocation, opt_allocation_std_dr, daily_return, cum_return, avg_daily_return, std_daily_return, sharpe_ratio


if __name__ == "__main__":
    symbols = ['AAPL', 'XOM', 'IBM', 'PG']
    start_date = '2020-09-01'
    end_date = '2021-05-31'
    allocations = np.array([0.3, 0.2, 0.4, 0.1])
    start_inv = 100000
    risk_free_rate = 0.0
    sampling_freq = 252

    optimize_portfolio(start_inv, risk_free_rate, sampling_freq, symbols, allocations, start_date, end_date, True)

