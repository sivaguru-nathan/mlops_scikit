
import os  
  
from celery import Celery  
from dataset import Dataset
from handler import Modelhandler
import uuid
from mongo_init import Modeldb

model_registry="model_registry"    
app = Celery('Mlops_app')  
  
# Load task modules  
app.autodiscover_tasks()  
  
@app.task(bind=True)  
def train(self,dataset_kwargs,model_kwargs,tuning=False,metric=None,iters=50):  
    data=Dataset(**dataset_kwargs)

    md = Modelhandler(**model_kwargs)
    x_train,x_test,y_train,y_test=data.train_test_split(0.3)
    md.fit(x_train,y_train,iters,tuning,metric)
    model_path=os.path.join("model_registry",uuid.uuid4().hex)
    md.save_model(md.model,model_path)
    model_parameters=md.model_params
    model_name=model_kwargs["model_name"]
    metrics=md.evaluate(x_test,y_test,metric)
    modeldb=Modeldb()
    _id=modeldb.create_record({"name":model_name,"parameters":model_parameters,"model_path":model_path,"metrics":metric})
    print(_id)

dataset_kwargs={"columns":["l3","l5"],"target":"target","file":"challenge.csv"}
model_kwargs={"model_type":"Regression","model_name":"random_forest"}

train.delay(dataset_kwargs,model_kwargs,tuning=True,metric="r2")