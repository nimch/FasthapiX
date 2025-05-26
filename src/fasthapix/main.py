"""
Main main
"""

import logging
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s :: %(message)s")

TEMPLATES_PATH = str(Path(__package__ + "/templates").absolute())
logger.debug(f"TEMPLATES_PATH={TEMPLATES_PATH}")

IMG_PATH = str(Path(__package__ + "/statics/img").absolute())
logger.debug(f"IMG_PATH={IMG_PATH}")

templates = Jinja2Templates(directory=str(TEMPLATES_PATH))

app = FastAPI()

app.mount("/img", StaticFiles(directory=str(IMG_PATH)), name="img")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"appname": "FasthapiX", "punchline": "just uvnother fast api python web applix"},
    )
