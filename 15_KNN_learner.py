import pandas as pd
import utils
from models.KNNLearner import KNNLearner

if __name__ == "__main__":
    window_size = 20
    symbols = ['XOM', 'PG']
    start_date = '2020-09-01'
    end_date = '2021-05-31'
    date_range = pd.date_range(start_date, end_date)

    prices_df: pd.DataFrame = utils.get_data(symbols, date_range)

    prices_df.fillna(method="ffill", inplace=True)
    prices_df.fillna(method="bfill", inplace=True)

    utils.plot_selected(prices_df, symbols, start_date, end_date)

    prices_symbols = prices_df[symbols]

    up_bound, lw_bound = utils.get_bollinger_band(utils.get_rolling_mean(prices_symbols, window_size), utils.get_rolling_std(prices_symbols, window_size))
    band_size = up_bound - lw_bound
    band_size.fillna(method="bfill", inplace=True)

    price_pct_change = prices_symbols.pct_change(periods=1)
    price_pct_change.fillna(method="bfill", inplace=True)

    df_x = pd.merge(band_size, price_pct_change, left_index=True, right_index=True)

    knn_clf = KNNLearner(5)
    knn_clf.train(df_x, prices_symbols)

    y_pred = pd.DataFrame(knn_clf.query(df_x), index=df_x.index, columns=['XOM', 'PG'])

    result_df = pd.merge(prices_symbols, y_pred, left_index=True, right_index=True)
    utils.plot_data(result_df[['XOM_x', 'XOM_y']])
    utils.plot_data(result_df[['PG_x', 'PG_y']])


