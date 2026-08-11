import hashlib, json

def recommendation_fingerprint(plan_ids: list[str], rounded_savings: float) -> str:
    payload = {"plan_ids": sorted(plan_ids), "rounded_savings": round(rounded_savings / 25) * 25}
    return hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
