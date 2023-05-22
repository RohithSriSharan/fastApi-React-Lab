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

 
#EXCEL 16 digit hexCode {    =TEXT(RANDBETWEEN(0,10^16-1),"0000000000000000")     }

ac = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Air Conditioners.csv")
ac_products = json.loads(ac.to_json(orient='records'))


# ac = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Air Conditioners.csv")
# ac_products = ac.to_json(orient='records')
appliances = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/All Appliances.csv")
appliance_products = json.loads(appliances.to_json(orient='records'))


carBike = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/All Car and Motorbike Products.csv")
carBike_products = json.loads(carBike.to_json(orient='records'))

electronics = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/All Electronics.csv")
electronics_products = json.loads(electronics.to_json(orient='records'))


fitness = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/All Exercise and Fitness.csv")
fitness_products = json.loads(fitness.to_json(orient='records'))


grocery = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/All Grocery and Gourmet Foods.csv")
grocery_products = json.loads(grocery.to_json(orient='records'))


homeKitchen = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/All Home and Kitchen.csv")
homeKitchen_products = json.loads(homeKitchen.to_json(orient='records'))


pet = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/All Pet Supplies.csv")
pet_products = json.loads(pet.to_json(orient='records'))

sportOutdoor = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/All Sports Fitness and Outdoors.csv")
sportOutdoor_products = json.loads(sportOutdoor.to_json(orient='records'))

amazonFashion = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Amazon Fashion.csv")
amazonFashion_products = json.loads(amazonFashion.to_json(orient='records'))


babyBath = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Baby Bath Skin and Grooming.csv")
babyBath_products = json.loads(babyBath.to_json(orient='records'))

babyFashion = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Baby Fashion.csv")
babyFashion_products = json.loads(babyFashion.to_json(orient='records'))

babyProducts = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Baby Products.csv")
babyProducts_products = json.loads(babyProducts.to_json(orient='records'))


backpacks = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Backpacks.csv")
backpacks_products = json.loads(backpacks.to_json(orient='records'))

badminton = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Badminton.csv")
badminton_products = json.loads(badminton.to_json(orient='records'))

bagLuggage = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Bags and Luggage.csv")
bagLuggage_products = json.loads(bagLuggage.to_json(orient='records'))

ballerina = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Ballerinas.csv")
ballerina_products = json.loads(ballerina.to_json(orient='records'))

beautyGrooming = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Beauty and Grooming.csv")
beautyGrooming_products = json.loads(beautyGrooming.to_json(orient='records'))

bedLinen = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/bed.csv")
bedLinen_products = json.loads(bedLinen.to_json(orient='records'))

# Create a dictionary to hold all the products data
products = {
    "air": ac_products,
    "appliance": appliance_products,
    "carbike": carBike_products,
    "electronics": electronics_products,
    "fitness": fitness_products,
    "grocery": grocery_products,
    "homekitchen": homeKitchen_products,
    "pet": pet_products,
    "sports": sportOutdoor_products,
    "amazonfashion": amazonFashion_products,
    "babygrooming": babyBath_products,
    "babyfashion":babyFashion_products,
    "babyproducts": babyProducts_products,
    "backpack":backpacks_products,
    "badminton":badminton_products,
    "bags-luggage":bagLuggage_products,
    "ballerina": ballerina_products,
    "beautyandgrooming":beautyGrooming_products,
    "bedroom-linen":bedLinen_products,

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




       