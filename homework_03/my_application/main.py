from fastapi import FastAPI
from views.ping_pong import router as ping_pong_router
from views.users.views import router as users_router

app = FastAPI()
app.include_router(ping_pong_router, tags=["Ping-pong"])
app.include_router(users_router, prefix="/players", tags=["Players"])


@app.get("/")
def root():
    return {"message": "Hello, World!"}
