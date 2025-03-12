from sklearn.base import RegressorMixin
import numpy as np

class MeanRegressor(RegressorMixin):
    # Predicts the mean of y_train
    def fit(self, X=None, y=None):
        self.fit_y = y.mean()

    def predict(self, X=None):
        return np.ones(X.shape[0]) * self.fit_y