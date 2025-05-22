"""
Main main
"""

import argparse
import logging
from importlib import import_module

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

logger = logging.getLogger()


templates = Jinja2Templates(directory="templates")

app = FastAPI()

app.mount("/img", StaticFiles(directory="img"), name="img")


def parse_args():
    parser = argparse.ArgumentParser(description="FasthapiX")

    parser.add_argument(
        "--launch-user",
        help="Launch user web app.",
        dest="launch_user",
        action="store_true",
    )
    parser.set_defaults(launch_user=True)

    parser.add_argument(
        "--debug",
        help="Display debugging information.",
        action="store_const",
        dest="loglevel",
        const=logging.DEBUG,
        default=logging.INFO,
    )

    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel, format="%(levelname)s :: %(message)s")

    return args


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"appname": "FasthapiX", "punchline": "just uvnother fast api python web applix"},
    )


def main():
    args = parse_args()
    logger.debug("Arguments parsed")

    if args.launch_user:
        users_module = import_module("users")
        users_app = users_module.main()
        app.include_router(
            users_app,
            prefix="/users",
        )

    return app


if __name__ == "__main__":
    main()
