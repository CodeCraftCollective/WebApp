from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
def homepage():
    return """
    <html>
    <head>
        <title>CodeCraft Collective</title>
    </head>
    <body>
        <h1>Welcome!</h1>
        <p>Use this website to make learning fun!</p>
    </body>
    </html>
    """
