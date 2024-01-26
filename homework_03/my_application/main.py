from fastapi import FastAPI
from views.url_paths import router as url_paths_router

app = FastAPI()
app.include_router(url_paths_router)


@app.get("/")
def root():
    return {"message": "Hello, World!"}
