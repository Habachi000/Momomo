import os
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from firebase_service import send_to_firebase 
from UpdateDataKey_HB import  update_data_key

app = FastAPI()

class UserPayload(BaseModel):
    text: str
    
class PlusCoinsPayload(BaseModel):
    text: str
    
class UbdatValue_FromKey(BaseModel):
    text: str
    id:str
    

@app.get("/")
async def test_get():
    import token_hb 
    return token_hb.root()

@app.post("/update-user")
async def update_firebase_user(data: UserPayload):
    result = send_to_firebase(data.text)
    return result

@app.post("/Update_DataKey")
async def UbdatData (data: UbdatValue_FromKey):
    result = update_data_key(data.id,data.text)
    return result





if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
@app.post("/PlusCoins-user")
async def Delet(data: UserPayload):
    result = update_data_key(data.text,data.id)
    return result

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
