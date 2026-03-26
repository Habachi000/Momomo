import requests
import token_hb
import json

def update_data_key(record_id: str, new_content: str):
    try:
        final_url = f"{token_hb.FIREBASE_URL}/{record_id}.json?auth={token_hb.MY_SECRET}"
        
        data = {"text": new_content}
        response = requests.patch(final_url, data=json.dumps(data), timeout=10)
        
        response.raise_for_status() 
        
        return {
            "status": "Updated Successfully",
            "Updated ID": record_id,
            "New Data": response.json()
        }
    except Exception as e:
        return {"err": str(e)}
