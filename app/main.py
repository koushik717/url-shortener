
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
import string, random

app = FastAPI()
url_db: Dict[str, str] = {}
analytics_db: Dict[str, int] = {}

class URLRequest(BaseModel):
    original_url: str

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.post("/shorten")
def shorten_url(request: URLRequest):
    short_code = generate_short_code()
    url_db[short_code] = request.original_url
    analytics_db[short_code] = 0
    return {"short_url": f"http://localhost:8000/{short_code}"}

@app.get("/{short_code}")
def redirect_url(short_code: str):
    if short_code not in url_db:
        raise HTTPException(status_code=404, detail="URL not found")
    analytics_db[short_code] += 1
    return {"original_url": url_db[short_code]}

@app.get("/analytics/{short_code}")
def get_analytics(short_code: str):
    if short_code not in analytics_db:
        raise HTTPException(status_code=404, detail="Analytics not found")
    return {"clicks": analytics_db[short_code]}
