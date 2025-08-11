
import json
import pickle
import numpy as np
import pandas as pd
import os

__locations = None
__data_columns = None
__model = None

def get_location_names():
    return __locations


def loaded_saved_artifacts():
    global __data_columns
    global __locations

    script_dir = os.path.dirname(__file__)
    artifacts_path = os.path.join(script_dir, 'artifacts')

    with open (os.path.join(artifacts_path, "columns.json"), 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    global __model
    if __model is None:
        with open(os.path.join(artifacts_path, "model.pickle"), 'rb') as f:
            __model = pickle.load(f)

def get_data_columns():
    return __data_columns   

def predict_price(location , sqft, bath, bhk):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    
    return round(__model.predict([x])[0], 2)




if __name__ == '__main__':
    loaded_saved_artifacts()
    