import pandas as pd
import json

def womenFashion():

    data = pd.read_csv('C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Air Conditioners.csv')

    products = data.head().to_json(orient='records')
    return json.loads(products) # convert to a Python object

