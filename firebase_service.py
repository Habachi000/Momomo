import requests
import token_hb

def send_to_firebase(text_content: str):
    try:
        final_url = f"{token_hb.FIREBASE_URL}?auth={token_hb.MY_SECRET}"
        
        payload = {
            "user_content": text_content,
            "timestamp": "2026-03-25" 
        }
        
        response = requests.post(final_url, json=payload, timeout=10)
        
        response.raise_for_status() 
        
        generated_id = response.json().get("name")
        return {"Id BY HabaChi : ": generated_id}
        
    except Exception as e:
        return {"err": str(e)}
