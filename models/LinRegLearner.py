import pandas as pd
from sklearn.linear_model import LinearRegression


class LinRegLearner:

    def __init__(self):
        self.reg = LinearRegression()
        pass

    def train(self, x: pd.DataFrame, y: pd.DataFrame):
        self.reg.fit(x, y)
        pass

    def query(self, x: pd.DataFrame) -> pd.DataFrame:
        return self.reg.predict(x)
