from fastapi import FastAPI
import uvicorn

from app.routers import news

app = FastAPI()

app.include_router(news.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the News Summary API"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8011, reload=True)