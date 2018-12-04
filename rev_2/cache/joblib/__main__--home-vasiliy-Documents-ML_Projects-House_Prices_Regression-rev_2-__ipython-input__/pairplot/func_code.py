# first line: 1
@memory.cache
def pairplot(train, live_area_cols):
    g = sns.pairplot(train[live_area_cols])
    g.map_diag(sns.kdeplot)
    g.map_offdiag(sns.regplot)
    return g
