# first line: 1
@memory.cache
def fit_predict(est, X, y):
    return est.fit(X, y).predict(X)
