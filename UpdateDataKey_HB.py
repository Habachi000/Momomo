import requests
import token_hb

def update_data_key(record_id: str, update_json_data: str):
    try:
        # 1. تنظيف الرابط الأساسي من أي سلاش زائدة في النهاية
        base_url = token_hb.FIREBASE_URL.strip().rstrip('/')
        
        # 2. تنظيف الـ ID من أي سلاش زائدة
        clean_id = record_id.strip().strip('/')
        
        # 3. بناء الرابط بدون بارامتر auth
        # الرابط النهائي سيكون: https://your-db.firebaseio.com/record_id.json
        url = f"{base_url}/{clean_id}.json"
        
        # 4. إرسال البيانات كـ JSON (سيقوم بتحديث حقل text فقط)
        payload = {"text": update_json_data}
        
        response = requests.patch(
            url, 
            json=payload, 
            timeout=10
        )
        
        if response.status_code == 200:
            return f"Done: {response.status_code}"
        else:
            # في حال ظهر خطأ 401 أو 403، فهذا يعني أن Firebase يطلب مفتاح السر (Rules)
            return f"Error: {response.status_code} - {response.text}"        
    except Exception as e:
        return f"Error: {str(e)}"
