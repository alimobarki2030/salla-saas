from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "✅ API is running"}

@app.get("/products")
async def get_products():
    return {"products": ["منتج 1", "منتج 2", "منتج 3"]}

