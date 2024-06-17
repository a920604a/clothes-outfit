from typing import Union
from typing import List, Dict
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from notification import logger
import uvicorn

app = FastAPI()


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8080",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


from frontend.api import router as api_router
app.include_router(api_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Hello World"}



# option 1
# uvicorn app:app --reload


# option 2
if __name__ == "__main__":
    uvicorn.run(app="app:app", host="127.0.0.1", port=8080, reload=True)
