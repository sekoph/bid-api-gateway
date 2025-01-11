from fastapi import Request, HTTPException
import httpx
from config import SERVICES_URL

# async def get_service_url(service_name: str):
#     return SERVICES_URL.get(service_name)

async def proxy_request(service_name: str, requests: Request):
    if service_name not in SERVICES_URL:
        raise HTTPException(status_code=404, detail="Service not found")
    
    url = f"{SERVICES_URL[service_name]}{requests.url.path}"
    
    print(f"Request URL: {url}")
    
    async with httpx.AsyncClient() as client:
        response = await client.request(
            requests.method,
            url,
            params=requests.query_params,
            json=await requests.json() if requests.method == ["POST", "PUT"] else None,
        )
    return response.json()