from fastapi import FastAPI, APIRouter, Request

import pandas as pd

router = APIRouter()

# Load products data
ac = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Air Conditioners.csv")
ac_products = ac.to_json(orient='records')

appliances = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Air Conditioners.csv")
appliance_products = appliances.to_json(orient='records')

# Create a dictionary to hold all the products data
products = {
    "air-conditioner": ac_products,
    "appliances": appliance_products
}

@router.post('/query')
async def search(request: Request):
    # Get request body and check if it is a JSON object
    try:
        data = await request.json()
    except ValueError:
        return {"error": "Invalid request body format. Must be a valid JSON object."}
    
    # Get search query from request body
    search_query = data.get("search")
    if not search_query:
        return {"error": "Search query not found in request body."}
    
    # Search for matching products in each category
    results = {}
    for category, products_json in products.items():
        products_list = pd.read_json(products_json)
        matching_products = products_list[products_list['name'].str.contains(search_query, case=False)]
        results[category] = matching_products.to_json(orient='records')
    print(results)
    return results


    

@router.get("/allproducts")
async def all_products():
    return products
