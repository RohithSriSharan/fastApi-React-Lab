from fastapi import FastAPI, APIRouter, Request

import pandas as pd

router = APIRouter()

# Load products data
#Air conditioners
ac = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Air Conditioners.csv")
ac_products = ac.to_json(orient='records')

#Appliances
appliances = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/All Appliances.csv")
appliance_products = appliances.to_json(orient='records')

#Car and Bike Products
carAndBike = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/All Car and Motorbike Products.csv")
carAndBike_products = carAndBike.to_json(orient='records')

#ALL ELECTRONICS
electronics = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/All Electronics.csv")
electronics_products = electronics.to_json(orient='records')

#ALL EXCERCISE AND FITNESS
fitness = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/All Exercise and Fitness.csv")
fitness_products = fitness.to_json(orient='records')

#Grocery
grocery = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/All Grocery and Gourmet Foods.csv")
grocery_products = grocery.to_json(orient='records')

#home And Kitchen
kitchen = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/All Home and Kitchen.csv")
kitchen_products = kitchen.to_json(orient='records')

#PET SUPPLIES
petSupplies = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/All Pet Supplies.csv")
petSupplies_products = petSupplies.to_json(orient='records')

#ALL SPORT FITNESS AND OUTDOORS
sportOutDoors = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/All Sports Fitness and Outdoors.csv")
sportOutDoors_products = sportOutDoors.to_json(orient='records')

#AMAZON FASHION
amzonFashion = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Amazon Fashion.csv")
amzonFashion_products = amzonFashion.to_json(orient='records')

#Amazon-Products
amazonProducts = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Amazon-Products.csv")
amazonProducts_products = amazonProducts.to_json(orient='records')

#BABY BATH SKIN AND GROOMING
babyBathAndGrooming = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Baby Bath Skin and Grooming.csv")
babyBathAndGrooming_products = babyBathAndGrooming.to_json(orient='records')

#BABY FASHION
babyFashion = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Baby Fashion.csv")
babyFashion_products = babyFashion.to_json(orient='records')


#BABY PRODUCTS
babyProducts = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Baby Products.csv")
babyProducts_products = babyProducts.to_json(orient='records')

#BACKPACKS
backPacks = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Backpacks.csv")
backPacks_products = backPacks.to_json(orient='records')

#BADMINTON
Badminton = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Badminton.csv")
Badminton_products = Badminton.to_json(orient='records')

#BACGS AND LUGGAGE
bagsAndLuggage = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Bags and Luggage.csv")
bagsAndLuggage_products = bagsAndLuggage.to_json(orient='records')

#BALLERINA
ballerina = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Ballerinas.csv")
ballerina_products = ballerina.to_json(orient='records')

#BEAUTY AND GROOMING
beautyGrooming = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Beauty and Grooming.csv")
beautyGrooming_products = beautyGrooming.to_json(orient='records')

#BEDROOM LINEN
bedroomLinen = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Bedroom Linen.csv")
bedroomLinen_products = bedroomLinen.to_json(orient='records')

#CAMERA ACCESSORIES
cameraAccesories = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Camera Accessories.csv")
cameraAccesories_products = cameraAccesories.to_json(orient='records')

#CAMERAS
cameras = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Cameras.csv")
cameras_products = cameras.to_json(orient='records')

#CAMPING AND HIKING
campingAndHiking = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Camping and Hiking.csv")
campingAndHiking_products = campingAndHiking.to_json(orient='records')

#Car Accessories
carAccessories = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Car Accessories.csv")
carAccessories_products = carAccessories.to_json(orient='records')

#CAR AND BIKE CARE
carAndBikeCare = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Car and Bike Care.csv")
carAndBikeCare_products = carAndBikeCare.to_json(orient='records')

#Car Electronics
carElectronics = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Car Electronics.csv")
carElectronics_products = carElectronics.to_json(orient='records')

#CAR PARTS
carParts = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Car Parts.csv")
carParts_products = carParts.to_json(orient='records')

#Cardio Equipment
cardiEquipment = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Cardio Equipment.csv")
cardiEquipment_products = cardiEquipment.to_json(orient='records')

#CASUAL SHOES
casualShoes = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Casual Shoes.csv")
casualShoes_products = casualShoes.to_json(orient='records')

#Clothing
clothing = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Clothing.csv")
clothing_products = clothing.to_json(orient='records')

#Cofee Tea And Beverages
coffeTeaBeverages = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Coffee Tea and Beverages.csv")
coffeTeaBeverages_products = coffeTeaBeverages.to_json(orient='records')

#Cricket
cricket = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Cricket.csv")
cricket_products = cricket.to_json(orient='records')

#CYCLING
cycling = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Cycling.csv")
cycling_products = cycling.to_json(orient='records')

#DIAPERS
diapers = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Diapers.csv")
diapers_products = diapers.to_json(orient='records')

#DIET AND NUTRITION
dietAndNutrition = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Diet and Nutrition.csv")
dietAndNutrition_products = dietAndNutrition.to_json(orient='records')

#DOG SUPPLIES
dogSupplies = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Dog supplies.csv")
dogSupplies_products = dogSupplies.to_json(orient='records')

#ETHNIC WEAR
ethnicWear = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Ethnic Wear.csv")
ethnicWear_products = ethnicWear.to_json(orient='records')

#FASHION AND SILVER JEWELLWEY
fashionAndSilverJewellery = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Fashion and Silver Jewellery.csv")
fashionAndSilverJewellery_products = fashionAndSilverJewellery.to_json(orient='records')

#FASHION SALES AND DEALS
fashionSaleAndDeals = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Fashion Sales and Deals.csv")
fashionSaleAndDeals_products = fashionSaleAndDeals.to_json(orient='records')

#FASHION SANDALS
fashionSandals = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Fashion Sandals.csv")
fashionSandals_products = fashionSandals.to_json(orient='records')

#FITNESS ACCESSORIES
fitnessAccessories = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Fitness Accessories.csv")
fitnessAccessories_products = fitnessAccessories.to_json(orient='records')

#FOOTBALL
football = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Football.csv")
football_products = football.to_json(orient='records')

#Formal Shoes
formalShoes = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Formal Shoes.csv")
formalShoes_products = formalShoes.to_json(orient='records')

#Furniture
furniture = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Furniture.csv")
furniture_products = furniture.to_json(orient='records')

#GARDEN AND OUTDOORS
gardenAndOutDoors = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Garden and Outdoors.csv")
gardenAndOutDoors_products = gardenAndOutDoors.to_json(orient='records')
#GOLD AND DIAMOND JEWELLERY
goldAndDiamond = pd.read_csv("C:/Users/rohit/OneDrive/Desktop/pythonWebApps/fastApi-react-lab/server/app/archive (15)/Gold and Diamond Jewellery.csv")
goldAndDiamond_products = goldAndDiamond.to_json(orient='records')


# Create a dictionary to hold all the products data
products = {
    "air-conditioner": ac_products,
    "appliances": appliance_products,
    "carAndBike": carAndBike_products,
    "electronics": electronics_products,
    "fitness": fitness_products,
    "grocery": grocery_products,
    "kitchen": kitchen_products,
    "petSupplies":petSupplies_products,
    "sportOutDoors":sportOutDoors_products,
    "amazonFashion": amzonFashion_products,
    "amazonProducts":amazonProducts_products,
    "babyBathAndGrooming":babyBathAndGrooming_products,
    "babyFashion": babyFashion_products,
    "babyProducts": babyProducts_products,
    "backPacks": backPacks_products,
    "badminton": Badminton_products,
    "bagsAndLuggage":bagsAndLuggage_products,
    "ballerina":ballerina_products,
    "beautyGrooming": beautyGrooming_products,
    "bedroomLinen": bedroomLinen_products,
    "cameraAccessories":cameraAccesories_products,
    "cameras":cameras_products,
    "campingAndHiking":campingAndHiking_products,
    "carAccessories":carAccessories_products,
    "carAndBikeCare":carAndBikeCare_products,
    "carElectronics":carElectronics_products,
    "carParts": carParts_products,
    "cardioEquipment":cardiEquipment_products,
    "casualShoes":casualShoes_products,
    "clothing":clothing_products,
    "coffeeTeaBeverages": coffeTeaBeverages_products,
    "cricket":cricket_products,
    "cycling":cycling_products,
    "diapers":diapers_products,
    "dietAndNutrition":dietAndNutrition_products,
    "dogSupplies":dogSupplies_products,
    "ethnicWear":ethnicWear_products,
    "fashionAndSilverJewellery":fashionAndSilverJewellery_products,
    "fashionSaleAndDeals":fashionSaleAndDeals_products,
    "fashionSandals":fashionSandals_products,
    "fitnessAccessories":fitnessAccessories_products,
    "football": football_products,
    "formalShoes": formalShoes_products,
    "furniture": furniture_products,
    "gardenAndOutDoors":gardenAndOutDoors_products,
    "goldAndDiamond": goldAndDiamond_products

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
