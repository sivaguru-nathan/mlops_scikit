import joblib
import models
from sklearn.model_selection import RandomizedSearchCV
import metrics

class Modelhandler:
    
    def __init__(self,model_type,model_name,model_params=None,model=None,**kwargs):
        if model!=None:
            self.model=self.model
        else:
            self.model,self.param_grid=getattr(getattr(model,model_type),model_name)()
        self.model_params=model_params
        self.model_type=model_type
             
    
    def load_model(self,model_path):
       
        model=joblib.load(model_path)
        return model
    
    def save_model(self,model,model_path):
        joblib.save(model,model_path)
    
    def hyperparameter_tuning(self,estimator,params,iters,metric):
        #hyper parameter tuning with random search
        random_cv = RandomizedSearchCV(
                estimator, params, n_iter=iters, scoring=metric, n_jobs=-1
            )
        return random_cv.best_params_
            
    def fit(self,X,Y,iters=50,tuning=False,metric=None):
        if tuning and self.model_params:
            self.param_grid.update(self.model_params)
        if tuning:
            self.model_params=self.hyperparameter_tuning(self.model,self.param_grid,iters,metric)
        self.model=self.model(**self.model_params)
        self.model=self.model.fit(X,Y)
        
    def predict(self,X):
        return self.model.predict(X)
    
    def evaluate(self,X,Y,metric):
        y_true=Y
        y_pred=self.predict(X)
        metric=getattr(getattr(metrics,self.model_type),metric)(y_true,y_pred)
        return metric