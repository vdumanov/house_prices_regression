# first line: 1
@memory.cache
def score_svr(X, y):
    svr = SVR(kernel='poly')
    scores = cross_val_score(svr, X, y, cv=10, scoring='neg_mean_squared_error')
    rmses = (-scores)**.5
    return (svr, np.mean(rmses), np.std(rmses))
