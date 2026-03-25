import os
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
# --- هنا عيطنا على الملف الجديد والفانكشن اللي فيه ---
from firebase_service import send_to_firebase 

app = FastAPI()

class UserPayload(BaseModel):
    text: str

@app.get("/")
async def test_get():
    import token_hb # حيت استعملتيه هنا
    return token_hb.root()

@app.post("/update-user")
async def update_firebase_user(data: UserPayload):
    # عيطنا على الخدمة من الملف الآخر وصيفطنا ليها غير النص
    result = send_to_firebase(data.text)
    return result

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
