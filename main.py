from fastapi import FastAPI, Response
import httpx

app = FastAPI()

BASE_URL = "https://image.pollinations.ai/prompt/"

@app.get("/generate-image/")
async def generate_image(prompt: str):
    image_url = f"{BASE_URL}{prompt}"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(image_url)
    
    if response.status_code == 200:
        return Response(content=response.content, media_type=response.headers["content-type"])
    else:
        return {"error": "Failed to fetch image"}, response.status_code
