import requests
import token_hb

def update_data_key(record_id: str, update_json_data: str):
    try:
        url = f"{token_hb.FIREBASE_URL}/{record_id}.json?auth={token_hb.MY_SECRET}"
        response = requests.patch(
            url, 
            data=update_json_data.encode('utf-8'), 
            headers={"Content-Type": "application/json"}
        )
        if response.status_code == 200:
            return f"Done: {response.status_code}"
        else:
            return f"Error: {response.status_code} - {response.text}"        
    except Exception as e:
        return f"Error: {str(e)}"
      
