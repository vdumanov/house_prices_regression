# first line: 1
@memory.cache
def search_neighbors(X, y):
    search = GridSearchCV(
        estimator=KNeighborsRegressor(),
        param_grid={ 
            'n_neighbors': [2, 4, 6, 8, 10, 12, 14, 16, 18],
            'weights': ['uniform', 'distance'],
            'p': [1, 2]
        },
        cv=10,
        scoring='neg_mean_squared_error',
        verbose=2
    )
    search.fit(X_scaled, y)
    return (search.best_estimator_, search.best_params_, (-search.best_score_)**.5)
