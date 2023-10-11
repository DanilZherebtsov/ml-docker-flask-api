from fastapi import FastAPI
import joblib
import numpy as np

model = joblib.load('app/model.joblib')

class_names = np.array(['setosa', 'versicolor', 'virginica'])

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Iris model API'}

@app.post('/predict')
def predict(data: dict):
    """
    Predicts the class of a given set of features.

    Args:
        data (dict): A dictionary containing the features to predict.
        e.g. {"features": [1, 2, 3, 4]}

    Returns:
        dict: A dictionary containing the predicted class.
    """        
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    class_name = class_names[prediction][0]
    return {'predicted_class': class_name}

