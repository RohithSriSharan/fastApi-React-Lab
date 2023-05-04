from fastapi import FastAPI, APIRouter, Request

import pandas as pd
import json
router = APIRouter()

# Load products data
#Air conditioners
# def ac():
#     ac = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Air Conditioners.csv")
#     ac_products = ac.to_json(orient='records')
#     return (json.loads(ac_products))

ac = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Air Conditioners.csv")
ac_products = json.loads(ac.to_json(orient='records'))


# ac = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Air Conditioners.csv")
# ac_products = ac.to_json(orient='records')
appliances = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/All Appliances.csv")
appliance_products = json.loads(appliances.to_json(orient='records'))


# Create a dictionary to hold all the products data
products = {
    "air": ac_products,
    "appliance": appliance_products
}

@router.post("/query")
async def get_query(request: Request):
    response = await request.json()
    search_param = response['search']
    print(search_param)
    filtered_products = []

    for key in products.keys():
        for product in products[key]:
            if search_param.lower() in product["name"].lower():
                filtered_products.append(product)
    print(filtered_products)
    return filtered_products



    

@router.get("/allproducts")
async def all_products():
    return products


@router.get("/search/{tag}/{id}")
async def searchInfo(tag:str ,id: int):
    print(id, tag)
    for product in products[tag]:
        if product["id"] == id:
            print(product)
            return product
    
    return {"message": "Product not found"}




       