from typing import Union
import unittest
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
async def homepage(request:Request):
    return templates.TemplateResponse("welcome.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def homepage(request:Request):
    return templates.TemplateResponse("login.html", {"request": request})
