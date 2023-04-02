from fastapi import Request, FastAPI
from models import User
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
   
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.get('/', response_model=User)
async def root():
    content = {'name': 'Rohith', "age":25}
    return content

@app.post('/')
async def root_1(request: Request):
    response = await request.json()
    username = response['username']
    print(username)
    return response

@app.get('/home')
async def home(request: Request):
    return 'Home'