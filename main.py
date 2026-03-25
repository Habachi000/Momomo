import requests
import uvicorn
import os  # ضروري باش نقراو المنفذ والساروت
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserPayload(BaseModel):
    text: str

# جلب المعلومات من إعدادات الاستضافة (Env Vars) أو استعمال القيم الافتراضية
# في الاستضافة، حط هاد المعلومات في خانة الـ Environment Variables
FIREBASE_URL = os.getenv("FIREBASE_URL", "https://follower-hb-default-rtdb.firebaseio.com/.json")
MY_SECRET = os.getenv("FIREBASE_SECRET", "Vem8760WElX5wFkflX9D0DsT9cznsPbGhrLseQtf")

@app.post("/update-user")
async def update_firebase_user(data: UserPayload):
    print(f"--- [Request Received] Text: {data.text} ---")
    try:
        # بناء الرابط
        final_url = f"{FIREBASE_URL}?auth={MY_SECRET}"
        payload = {"user": data.text}
        
        # إرسال لـ Firebase (PUT يمسح القديم ويحط الجديد)
        response = requests.put(final_url, json=payload, timeout=15)
        
        return {
            "status": "success", 
            "firebase_code": response.status_code
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    # الاستضافة كتعطينا المنفذ في متغير سميتو PORT
    port = int(os.getenv("PORT", 8000))
    # كنخدمو بـ 0.0.0.0 باش السيرفر يقبل اتصالات من "برا"
    uvicorn.run(app, host="0.0.0.0", port=port)
