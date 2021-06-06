import utils
import pandas as pd

if __name__ == "__main__":
    symbols = ['FAKE1', 'FAKE2']
    dates = pd.date_range('2017-03-14', '2018-03-13')
    df: pd.DataFrame = utils.get_data(symbols, dates)
    df.fillna(method='ffill', inplace=True)
    df.fillna(method='bfill', inplace=True)
    utils.plot_data(df)