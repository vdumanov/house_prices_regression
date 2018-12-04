# first line: 1
@memory.cache
def score_xgb(X, y):
    search = GridSearchCV(
        estimator=xgb.XGBRegressor(random_state=42, n_jobs=-1),
        param_grid={ 
            'n_estimators': [500, 1000, 1500],
            'learning_rate': [.5, .1, .3],
            'max_depth': [2, 5, 10]
        },
        cv=10,
        scoring='neg_mean_squared_error',
        verbose=2
    )
    search.fit(X, y)
    return (search.best_estimator_, search.best_params_, (-search.best_score_)**.5)
