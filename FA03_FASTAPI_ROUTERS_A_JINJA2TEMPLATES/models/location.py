from pydantic import BaseModel
from typing import Optional

class Location(BaseModel):  # Model Dat
    mesto: str
    lat: Optional[float] = None
    lon: Optional[float] = None

class DajSiMikinu(BaseModel):
    temp: float
    daj_si_mikinu: bool


