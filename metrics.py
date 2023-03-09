class Regression:
    def r2(self,y_true,y_predict):
        from sklearn.metrics import r2_score
        return r2_score(y_true, y_pred)