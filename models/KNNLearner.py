import pandas as pd
from sklearn.neighbors import KNeighborsRegressor


class KNNLearner:

    def __init__(self, k: int):
        self.reg = KNeighborsRegressor(n_neighbors=k)
        pass

    def train(self, x: pd.DataFrame, y: pd.DataFrame):
        self.reg.fit(x, y)
        pass

    def query(self, x: pd.DataFrame) -> pd.DataFrame:
        return self.reg.predict(x)
