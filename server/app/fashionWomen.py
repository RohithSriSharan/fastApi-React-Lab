import pandas as pd
import json
from fastapi import FastAPI, requests, APIRouter

router = APIRouter()

def womenFashion():

    data = pd.read_csv('C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Womens Fashion.csv')

    products = data.head().to_json(orient='records')
    return json.loads(products) # convert to a Python object

@router.get("/women/fashion")
async def product():
    products = womenFashion()
    print(products)
    return products
    



@router.get("/women/fashion/{product_id}")
async def get_product(product_id: int):
    products = womenFashion()
    for product in products:
        if product["id"] == product_id:
            return product
    return {"message": "Product not found"}