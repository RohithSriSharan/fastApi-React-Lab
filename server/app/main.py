from fastapi import Request,Response, FastAPI, HTTPException, status, Depends
from models import User
from fastapi.middleware.cors import CORSMiddleware
from mongoDB import user_collection
from passlib.context import CryptContext
from fastapi.security import OAuth2, OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from datetime import datetime, timedelta



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

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

OAuth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


# Password  bcrypt, hashing and verifying
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_pwd(password):
    return pwd_context.hash(password)

def verify_pwd(plain_pwd, hashed_pwd):
    return pwd_context.verify(plain_pwd, hashed_pwd)

# User get user 
#Takes a username from form and checks if the user is present in the db
def get_user(username):
    user = user_collection.find_one({'username': username })
    if not user:
        return False
    else: 
        return user

#if the user is found now we authenticate if the username and password matches
def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return 'Wrong creds'
    if not verify_pwd(password, user['password']):   
        return 'Wrong creds'
    return 'Authenticated'



#Now that we have the user name and password verified we then create an access TOKEN
##################### AUTHENTICATION / AUTHORIZATION #################################

def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt   

#Getting current User
def get_current_user(token: str = Depends(OAuth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY,algorithms=ALGORITHM)
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")
    except JWTError :
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")
    user = get_user(username)
    if user is None:
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")
    return user


#CURRENT ACTIVE USER
def get_current_active_user(current_user:dict = Depends(get_current_user)):
    if not current_user['is active']:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")
    return current_user


#####################################################################################

@app.get('/')
async def root():
    content = {"connection": "success"}
    return content



#REGISTER
@app.post('/register')
async def register(request: Request):
    registerForm_response = await request.json() #Get data from front end
    username = registerForm_response['email'] 
    password = registerForm_response['password']
    encrypted_pwd = hash_pwd(password) #hash the password
    userInDB = get_user(username)  #Check for user in db 
    if userInDB:                    #If username exists
        return "User already exists"
    else:                           #If username doesnot exist
        content = {'username': username, 'password': encrypted_pwd}
        user_collection.insert_one(content)
        return 'Registered successfully'

# # LOG_IN
# @app.post('/')
# async def login(request: Request):
#     loginForm_response = await request.json()
#     login_username = loginForm_response['username']
#     login_password = loginForm_response['password']
#     logging_user = authenticate_user(login_username,login_password)
#     return logging_user




# @app.get('/home')
# async def home(request: Request):
#     return 'Home'

@app.post('/login')
async def login(request: Request):
    loginForm_response = await request.json()
    login_username = loginForm_response['username']
    login_password = loginForm_response['password']
    user = get_user(login_username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    elif not verify_pwd(login_password, user['password']):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
    else:
        access_token = create_access_token(data={"sub": user['username']}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
        print(access_token)
        response = Response()
        response.headers['Authorization'] = f"Bearer {access_token}"
        return {'access_token': access_token, 'token_type': 'bearer'}
        
@app.get('/home')
async def home(current_user: User = Depends(get_current_active_user), token: str = Depends(OAuth2_scheme)):
    return {'message': 'Hello, ' + current_user['username']}
