import urllib.request
import json

base = "http://127.0.0.1:3000"

# 1. Test Meta verification challenge (GET)
meta_url = f"{base}/api/webhook/meta?hub.mode=subscribe&hub.challenge=test_meta_challenge_12345&hub.verify_token=neonex_meta_leads_secret_2026"
req = urllib.request.Request(meta_url)
try:
    with urllib.request.urlopen(req) as resp:
        body = resp.read().decode('utf-8')
        print(f"Meta Verify Challenge: Status {resp.status}, Body: {body}")
except Exception as e:
    print(f"Meta Verify Challenge Failed: {e}")

# 2. Test Meta Lead Ingestion (POST)
meta_post_url = f"{base}/api/webhook/meta"
meta_payload = {
    "name": "Karthik Raja",
    "phone": "+91 94480 12345",
    "email": "karthik.raja.eng@gmail.com",
    "program": "Data Science & AI Master Program",
    "campaign_name": "Bengaluru_DataScience_LeadGen_Nov2026",
    "ad_name": "QA_to_AI_Carousel_Ad_03",
    "notes": "Looking for weekend batch with placement assistance"
}
req = urllib.request.Request(
    meta_post_url,
    data=json.dumps(meta_payload).encode('utf-8'),
    headers={"Content-Type": "application/json"}
)
try:
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        print(f"Meta Lead Ingestion: {res}")
except Exception as e:
    print(f"Meta Lead Ingestion Failed: {e}")

# 3. Test Google Ads Lead Ingestion (POST)
google_post_url = f"{base}/api/webhook/google-ads"
google_payload = {
    "name": "Ananya Sen",
    "phone": "+91 98860 54321",
    "email": "ananya.sen.b@gmail.com",
    "program": "Data Analytics Master Program",
    "campaign_name": "Search_Data_Analytics_Course_Bengaluru",
    "notes": "Transitioning from non-IT to Data Analytics. Needs EMI options.",
    "user_column_data": [
        {"column_name": "FULL_NAME", "string_value": "Ananya Sen"},
        {"column_name": "PHONE_NUMBER", "string_value": "+91 98860 54321"},
        {"column_name": "EMAIL", "string_value": "ananya.sen.b@gmail.com"}
    ]
}
req = urllib.request.Request(
    google_post_url,
    data=json.dumps(google_payload).encode('utf-8'),
    headers={"Content-Type": "application/json"}
)
try:
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        print(f"Google Ads Lead Ingestion: {res}")
except Exception as e:
    print(f"Google Ads Lead Ingestion Failed: {e}")

# 4. Check CRM data has both leads recorded
crm_url = f"{base}/api/crm/data"
req = urllib.request.Request(crm_url)
try:
    with urllib.request.urlopen(req) as resp:
        cdata = json.loads(resp.read().decode('utf-8'))
        leads = cdata.get("enquiries", [])
        print(f"Total Enquiries in CRM: {len(leads)}")
        for l in leads:
            print(f" - [{l.get('utm_source')}] {l.get('name')} | {l.get('phone')} | {l.get('program')}")
except Exception as e:
    print(f"CRM Check Failed: {e}")
