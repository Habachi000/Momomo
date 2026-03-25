import requests
import os
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserPayload(BaseModel):
    text: str

# معلومات Firebase (يفضل وضعها في Env Vars في Vercel)
FIREBASE_URL = "https://follower-hb-default-rtdb.firebaseio.com/login.json"
MY_SECRET = "Vem8760WElX5wFkflX9D0DsT9cznsPbGhrLseQtf"

@app.get("/")
async def root():
    return {"status": "ســـــرفر يعمـــل ✨💕 HabaChi HB"}

@app.post("/update-user")
async def update_firebase_user(data: UserPayload):
    try:
        # إضافة الساروت للرابط
        final_url = f"{FIREBASE_URL}?auth={MY_SECRET}"
        
        # البيانات التي سيتم تخزينها داخل الـ ID التلقائي
        payload = {
            "user_content": data.text,
            "timestamp": "2026-03-25" # يمكنك استخدام مكتبة datetime لجعل الوقت حقيقياً
        }
        
        # استعمال POST لإنشاء ID تلقائي (Push ID) من طرف Firebase
        response = requests.post(final_url, json=payload, timeout=10)
        
        # إرجاع الـ ID الجديد الذي أنشأه Firebase للتطبيق
        generated_id = response.json().get("name")
        
        return {
            "status": "success", 
            "firebase_id": generated_id
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
    port = int(os.getenv("PORT", 8000))
    # كنخدمو بـ 0.0.0.0 باش السيرفر يقبل اتصالات من "برا"
    uvicorn.run(app, host="0.0.0.0", port=port)
