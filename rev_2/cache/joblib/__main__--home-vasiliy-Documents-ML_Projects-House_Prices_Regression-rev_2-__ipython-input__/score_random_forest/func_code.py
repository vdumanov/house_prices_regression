# first line: 1
@memory.cache
def score_random_forest(X, y):
    rfr = RandomForestRegressor(
        max_depth=100,
        max_features='sqrt',
        min_samples_leaf=1,
        min_samples_split=2,
        n_estimators=500,
        random_state=42
    )
    scores = cross_val_score(rfr, X, y, cv=10, scoring='neg_mean_squared_error')
    rmses = (-scores)**.5
    return (rfr, np.mean(rmses), np.std(rmses))
