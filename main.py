from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from services_router import proxy_request


app = FastAPI()

origins = [
    "http://localhost:8002",
    "http://localhost:8003",
    "http://localhost:8001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/{service_name}/{path:path}")
async def proxy_get(service_name: str, path: str, request: Request):
    return await proxy_request(service_name, request)

@app.post("/{service_name}/{path:path}")
async def proxy_post(service_name: str, path: str, request: Request):
    return await proxy_request(service_name, request)

@app.put("/{service_name}/{path:path}")
async def proxy_put(service_name: str, path: str, request: Request):
    return await proxy_request(service_name, request)

# @app.get("/{service_name}/{path:path}")
# async def proxy(service_name: str, path: str, request: Request):
#     return await proxy_request(service_name, request)

@app.delete("/{service_name}/{path:path}")
async def proxy_delete(service_name: str, path: str, request: Request):
    return await proxy_request(service_name, request)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)