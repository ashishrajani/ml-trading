import utils
import pandas as pd

if __name__ == "__main__":
    start_date = "2020-05-03"
    end_date = "2021-06-03"
    dates = pd.date_range(start_date, end_date)

    symbols = ["SPY", "GOOG", "IBM", "GLD"]
    symbols.sort()

    df = utils.get_data(symbols, dates)

    # print(df)
    # print(df.loc['2021-04-01':'2021-04-30'])
    # print(df['GOOG'])
    # print(df[['GOOG', 'GLD']])
    # print(df.loc['2021-04-01':'2021-04-05', ['GOOG', 'GLD']])

    # plot_data(df, "Stock Price")

    utils.plot_selected(df, symbols, start_date, end_date)
