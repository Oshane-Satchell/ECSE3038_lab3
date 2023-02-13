import urllib 
import pydantic
import motor.motor_asyncio
from bson import ObjectId
from datetime import datetime
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request, HTTPException



app = FastAPI()

origins = [
    
    "https://ecse3038-lab3-tester.netlify.app", "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://satchell_di_attican:" + urllib.parse.quote("Studentatti@07") + "@cluster0.z9m3nd2.mongodb.net/?retryWrites=true&w=majority")

db = client.water_tank
tanks_collection = db["tanks"]
profiles_collection = db["profiles"]


pydantic.json.ENCODERS_BY_TYPE[ObjectId]=str

@app.get("/profile")
async def get_profile():
    profile = await db["profile"].find().to_list(999)
    if len(profile) < 1:
        return {}
    return profile[0]


@app.post("/profile",status_code=201)
async def profilenew(request:Request):
    
    Result = await request.json()
    Result["last_updated"]=datetime.now()

    profile_new = await db["profile"].insert_one(Result)
    profile_create= await db["profile"].find_one({"_id": profile_new.inserted_id})

    return profile_create


@app.post("/data",status_code=201)
async def profilenew(request:Request):
    Tankobject = await request.json()

    tank_new = await db["tank"].insert_one(Tankobject)
    tank_cus = await db["tank"].find_one({"_id": tank_new.inserted_id})
    return tank_cus

    
@app.get("/data")
async def retrive_tanks():
    tanks = await db["tank"].find().to_list(999)
    return tanks

    
@app.patch("/data/{id}")
async def do_update(id:str, request: Request):
    new= await request.json()
    new_tank = await db["tank"].update_one({"_id":ObjectId(id)}, {'$set': new})
    
    if new_tank.modified_count == 1:
         if (
                tank_curr := await db["tank"].find_one({"_id": id})
            ) is not None:
                return tank_curr   
    else:
         raise HTTPException(status_code=404, detail="Item was not found")


@app.delete("/data/{id}",status_code=204)
async def delete_tank(id: str):

   tank_deleted = await db["tank"].find_one({"_id": ObjectId(id)})
   tank_removed = await db["tank"].delete_one({"_id":ObjectId(id)})