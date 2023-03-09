import numpy as np
class Regression:
    def random_forest(self):
        #random forest implementation
        from sklearn.ensemble import RandomForestRegressor
        model = RandomForestRegressor()
        n_estimators = np.arange(10, 200, step=10)
        max_features = ["auto", "sqrt", "log2"]
        max_depth = list(np.arange(10, 100, step=10)) + [None]
        min_samples_split = np.arange(2, 10, step=2)
        min_samples_leaf = [1, 2, 4]
        bootstrap = [True, False]
        param_grid = {
            "n_estimators": n_estimators,
            "max_features": max_features,
            "max_depth": max_depth,
            "min_samples_split": min_samples_split,
            "min_samples_leaf": min_samples_leaf,
            "bootstrap": bootstrap,
        }
        return model,param_grid
    
    def svm(self):
        #svm implementation
        from sklearn.svm import SVR
        model = SVR()
        kernel = ["linear", "rbf", "sigmoid", "poly"]
        tolerance = [1e-3, 1e-4, 1e-5, 1e-6]
        C = [1, 1.5, 2, 2.5, 3]
        param_grid = dict(kernel=kernel, tol=tolerance, C=C)
        return model,param_grid