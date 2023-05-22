import pandas as pd
import json
from fastapi import FastAPI, requests, APIRouter

router = APIRouter()

def appliances():

    data = pd.read_csv('C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/All Appliances .csv')

    products = data.to_json(orient='records')
    return json.loads(products) # convert to a Python object

@router.get("/appliances")
async def product():
    products = appliances()
    print(products)
    return products
    



@router.get("/appliances/{product_id}")
async def get_product(product_id: int):
    products = appliances()
    for product in products:
        if product["id"] == product_id:
            return product
    return {"message": "Product not found"}