# first line: 1
@memory.cache
def score_linear_regression(X, y):
    lr = LinearRegression()
    scores = cross_val_score(lr, X, y, cv=10, scoring='neg_mean_squared_error')
    rmses = (-scores)**.5
    return (lr, np.mean(rmses), np.std(rmses))
