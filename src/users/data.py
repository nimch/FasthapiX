from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    id: int
    firstname: str
    lasttname: str
    username: str
    email: str
    signup_ts: datetime | None
