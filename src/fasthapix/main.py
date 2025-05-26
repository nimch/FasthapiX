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

ALPINEJS_PATH = str(Path(__package__ + "/statics/alpinejs").absolute())
logger.debug(f"ALPINEJS_PATH={ALPINEJS_PATH}")

CSS_PATH = str(Path(__package__ + "/statics/css").absolute())
logger.debug(f"CSS_PATH={CSS_PATH}")

HTMX_PATH = str(Path(__package__ + "/statics/htmx").absolute())
logger.debug(f"HTMX_PATH={HTMX_PATH}")

templates = Jinja2Templates(directory=str(TEMPLATES_PATH))

app = FastAPI()

app.mount("/img", StaticFiles(directory=str(IMG_PATH)), name="img")
app.mount("/htmx", StaticFiles(directory=str(HTMX_PATH)), name="htmx")
app.mount("/alpinejs", StaticFiles(directory=str(ALPINEJS_PATH)), name="alpinejs")
app.mount("/css", StaticFiles(directory=str(CSS_PATH)), name="css")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"appname": "FasthapiX", "punchline": "just uvnother fast api python web applix"},
    )
