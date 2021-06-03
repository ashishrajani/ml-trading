import pandas as pd
import os
import matplotlib.pyplot as plt


def symbol_to_path(symbol, base_dir="data"):
    return os.path.join(base_dir, f"{str(symbol)}.csv")


def get_df(data_frame, symbol, columns, jhow="left"):
    path = symbol_to_path(symbol)
    df_temp = pd.read_csv(path,
                          index_col="Date",
                          parse_dates=True,
                          usecols=columns,
                          na_values=["nan"])
    df_temp = df_temp.rename(columns={columns[1]: symbol})
    data_frame = data_frame.join(df_temp, how=jhow)
    return data_frame


def get_data(symbols, dates):
    data_frame = pd.DataFrame(index=dates)

    if "SPY" in symbols:
        symbols.pop(symbols.index("SPY"))
    data_frame = get_df(data_frame, "SPY", ["Date", "Adj Close"], jhow="inner")

    for s in symbols:
        data_frame = get_df(data_frame, s, ["Date", "Adj Close"])

    return data_frame


def plot_data(df, title="Stock prices"):
    df.plot(figsize=(20, 15), fontsize=15)
    plt.title(title, fontsize=50)
    plt.ylabel("Price [$]", fontsize=20)
    plt.xlabel("Dates", fontsize=20)
    plt.legend(fontsize=20)
    plt.show()


def plot_selected(df, columns, start_date, end_date):
    plt_df = normalize_data(df.loc[start_date:end_date][columns])
    plot_data(plt_df)


def normalize_data(df):
    return df / df.iloc[0, :]
