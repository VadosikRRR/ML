from sklearn.base import ClassifierMixin
from scipy.stats import mode
import numpy as np

class MostFrequentClassifier(ClassifierMixin):
    # Predicts the rounded (just in case) median of y_train
    def fit(self, X=None, y=None):
        self.fit_y = mode(y)[0]

    def predict(self, X=None):
        return np.ones(X.shape[0]) * self.fit_y