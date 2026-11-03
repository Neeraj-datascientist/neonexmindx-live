import json
import os

crm_path = os.path.join("deployment_NeoNex", "data", "crm_data.json")
mirror_path = os.path.join("finalised_deployment", "data", "crm_data.json")

def clean_file(path):
    if not os.path.exists(path):
        print(f"Not found: {path}")
        return
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Filter enquiries: remove test/fake records (e.g., pooja.sharma.test, test phones, fake placeholder names)
    initial_count = len(data.get("enquiries", []))
    cleaned_enquiries = [
        e for e in data.get("enquiries", [])
        if "test" not in (e.get("email") or "").lower()
        and "test" not in (e.get("name") or "").lower()
        and (e.get("phone") or "").strip() != "+91 98765 43210"
        and (e.get("phone") or "").strip() != "9876543210"
    ]
    data["enquiries"] = cleaned_enquiries
    
    # Ensure integrations keys exist and are ready for live webhook consumption
    if "integrations" not in data:
        data["integrations"] = {}
    data["integrations"].setdefault("whatsappApiKey", "")
    data["integrations"].setdefault("whatsappPhoneId", "918431803839")
    data["integrations"].setdefault("whatsappTemplate", "welcome_counselling_lead_v1")
    data["integrations"].setdefault("metaVerifyToken", "neonex_meta_leads_secret_2026")
    data["integrations"].setdefault("metaAppSecret", "")
    data["integrations"].setdefault("googleAdsWebhookKey", "nx_gads_lead_token_2026")
    data["integrations"].setdefault("googleCustomerId", "606-542-9317")
    data["integrations"].setdefault("activeMetaCampaigns", [
        {
            "id": "meta-camp-01",
            "name": "Bengaluru_DataScience_LeadGen_Nov2026",
            "status": "Ready",
            "platform": "Meta (FB / IG Lead Ads)",
            "leads": 0,
            "cost_per_lead": "₹145 - ₹180 est.",
            "target": "QA, Support Engineers, College Grads"
        },
        {
            "id": "meta-camp-02",
            "name": "PowerBI_Tableau_FastTrack_Nov2026",
            "status": "Ready",
            "platform": "Instagram Reels Ad",
            "leads": 0,
            "cost_per_lead": "₹110 - ₹140 est.",
            "target": "Working Professionals (BPO/Operations to Analytics)"
        }
    ])
    data["integrations"].setdefault("activeGoogleCampaigns", [
        {
            "id": "gads-camp-01",
            "name": "Search_Data_Analytics_Course_Bengaluru",
            "status": "Ready",
            "platform": "Google Search & Lead Form",
            "leads": 0,
            "target_cpa": "₹320 est.",
            "keywords": ["data analytics course in bangalore", "data science institute near me", "offline data analytics coaching"]
        }
    ])
    
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Cleaned {path}: {initial_count} -> {len(cleaned_enquiries)} enquiries. Integrations ready.")

clean_file(crm_path)
clean_file(mirror_path)
