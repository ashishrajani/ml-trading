import pandas as pd
import matplotlib.pyplot as plt


def read_dataset(file_name: str) -> pd.DataFrame:
    return pd.read_csv(file_name)


def get_max(df: pd.DataFrame, attribute: str) -> float:
    return df[attribute].max()


def get_mean(df: pd.DataFrame, attribute: str) -> float:
    return df[attribute].mean()


def plot(df: pd.DataFrame, attribute: str):
    df[attribute].plot()
    plt.show()


def plot_multiple(df: pd.DataFrame, attr1: str, attr2: str):
    df[[attr1, attr2]].plot()
    plt.show()


if __name__ == "__main__":
    data = read_dataset("data/AAPL.csv")

    print(data.head(5))

    print(data[10:21])

    print('Max Close: ', get_max(data, 'Close'))

    print('Mean Volume: ', get_mean(data, 'Volume'))

    plot(data , 'Adj Close')

    plot(data, 'High')

    plot_multiple(data, 'Close', 'Adj Close')
