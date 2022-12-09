from fastapi import FastAPI
from typing import Union
import db


app = FastAPI()

db.information()
db.plusData()