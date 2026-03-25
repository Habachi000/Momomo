import requests
import os
from fastapi import FastAPI
from pydantic import BaseModel
import  token_hb
app = FastAPI()

class UserPayload(BaseModel):
    text: str
    
@app.get("/")
async def Test_GET():
    return token_hb.root()

@app.post("/update-user")
async def update_firebase_user(data: UserPayload):
    try:
        final_url = f"{token_hb.FIREBASE_URL}?auth={token_hb.MY_SECRET}"
        
        payload = {
            "user_content": data.text,
            "timestamp": "2026-03-25" 
        }
        
        response = requests.post(final_url, json=payload, timeout=10)
        generated_id = response.json().get("name")
        
        return {
            "status": "success", 
            "firebase_id": generated_id
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
        return {
            "status": "success", 
            "firebase_id": generated_id
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
    port = int(os.getenv("PORT", 8000))
    # كنخدمو بـ 0.0.0.0 باش السيرفر يقبل اتصالات من "برا"
    uvicorn.run(app, host="0.0.0.0", port=port)
